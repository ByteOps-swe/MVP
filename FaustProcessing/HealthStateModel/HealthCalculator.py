import threading
from datetime import datetime
from typing import List

from .ListaMisurazioni import ListaMisurazioni
from .MisurazioneSalute import MisurazioneSalute
from .Incrementers.TemperatureIncrementer import TemperatureIncrementer
from .Incrementers.HumidityIncrementer import HumidityIncrementer
from .Incrementers.DustPM10Incrementer import DustPM10Incrementer
from .HealthAlgorithm import HealthAlgorithm
from .SensorTypes import SensorTypes
class HealthCalculator(HealthAlgorithm):
    __tmpInc = TemperatureIncrementer()
    __umdInc = HumidityIncrementer()
    __dstPm10Inc = DustPM10Incrementer()
    __temperature_measure_type_naming = SensorTypes.TEMPERATURE.value
    __humidity_measure_type_naming = SensorTypes.HUMIDITY.value
    __dtsPm10_measure_type_naming = SensorTypes.DUST_PM10.value
    __healthScore_measure_type_naming = SensorTypes.HEALTH_SCORE.value

    def __init__(self):
        self.__listaMisurazioni = ListaMisurazioni() 
        self.__lock = threading.Lock()

    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        with self.__lock:
            self.__listaMisurazioni.add_misurazione(timestamp, value, type_, latitude, longitude, ID_sensore, cella)

    def generate_new_health_score(self)->List[MisurazioneSalute]:
        health_scores = []
        with self.__lock:
            for cella in self.__listaMisurazioni.get_unique_celle():
                punteggio_cella = (
                    HealthCalculator.__calcola_incremento_tmp(cella, self.__listaMisurazioni) +
                    HealthCalculator.__calcola_incremento_umd(cella, self.__listaMisurazioni) +
                    HealthCalculator.__calcola_incremento_dstPm10(cella, self.__listaMisurazioni)
                )
                health_scores.append(MisurazioneSalute(datetime.now(), punteggio_cella, self.__healthScore_measure_type_naming, cella))
            self.__listaMisurazioni.clear_list()
            return health_scores

    @staticmethod
    def __calcola_incremento_tmp(cella: str, listaMisurazioni):
        return HealthCalculator.__tmpInc.get_incrementation(
            listaMisurazioni.get_list_by_cella_and_type(cella, HealthCalculator.__temperature_measure_type_naming))

    @staticmethod
    def __calcola_incremento_umd(cella: str, listaMisurazioni):
        return HealthCalculator.__umdInc.get_incrementation(
            listaMisurazioni.get_list_by_cella_and_type(cella, HealthCalculator.__humidity_measure_type_naming))

    @staticmethod
    def __calcola_incremento_dstPm10(cella: str, listaMisurazioni):
        return HealthCalculator.__dstPm10Inc.get_incrementation(
            listaMisurazioni.get_list_by_cella_and_type(cella, HealthCalculator.__dtsPm10_measure_type_naming))
