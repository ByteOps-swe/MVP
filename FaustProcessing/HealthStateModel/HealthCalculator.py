import threading
from datetime import datetime
from typing import List

from .MisurazioneSalute import MisurazioneSalute
from .Incrementers.TemperatureIncrementer import TemperatureIncrementer
from .Incrementers.HumidityIncrementer import HumidityIncrementer
from .Incrementers.DustPM10Incrementer import DustPM10Incrementer
from .HealthAlgorithm import HealthAlgorithm
from .HealthProcessorBuffer import HealthProcessorBuffer
from .SensorTypes import SensorTypes

class HealthCalculator(HealthAlgorithm, HealthProcessorBuffer):
    __tmpInc = TemperatureIncrementer()
    __umdInc = HumidityIncrementer()
    __dstPm10Inc = DustPM10Incrementer()
    __temperature_measure_type_naming = SensorTypes.TEMPERATURE.value
    __humidity_measure_type_naming = SensorTypes.HUMIDITY.value
    __dtsPm10_measure_type_naming = SensorTypes.DUST_PM10.value
    __healthScore_measure_type_naming = SensorTypes.HEALTH_SCORE.value

    def __init__(self):
        self.__lock = threading.Lock()
        super().__init__()

    def generate_new_health_score(self)->List[MisurazioneSalute]:
        health_scores = []
        with self.__lock:
            for cella in super().get_lista_misurazioni().get_unique_celle():
                punteggio_cella = (
                    HealthCalculator.__calcola_incremento_tmp(cella, super().get_lista_misurazioni()) +
                    HealthCalculator.__calcola_incremento_umd(cella, super().get_lista_misurazioni()) +
                    HealthCalculator.__calcola_incremento_dstPm10(cella, super().get_lista_misurazioni())
                )
                health_scores.append(MisurazioneSalute(datetime.now(), punteggio_cella, self.__healthScore_measure_type_naming, cella))
            super().clear_list()
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
