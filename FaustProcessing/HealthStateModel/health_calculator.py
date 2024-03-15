import threading
from datetime import datetime
from typing import List

from .lista_misurazioni import lista_misurazioni
from .misurazione_salute import misurazione_salute
from .Incrementers.temperature_incrementer import temperature_incrementer
from .Incrementers.humidity_incrementer import humidity_incrementer
from .Incrementers.dust_PM10_incrementer import dust_PM10_incrementer
from .health_algorithm import health_algorithm
from .sensor_types import sensor_types

class health_calculator(health_algorithm):
    __tmpInc = temperature_incrementer()
    __umdInc = humidity_incrementer()
    __dstPm10Inc = dust_PM10_incrementer()
    __temperature_measure_type_naming = sensor_types.TEMPERATURE.value
    __humidity_measure_type_naming = sensor_types.HUMIDITY.value
    __dtsPm10_measure_type_naming = sensor_types.DUST_PM10.value
    __health_score_measure_type_naming = sensor_types.HEALTH_SCORE.value

    def __init__(self):
        self.__listaMisurazioni = lista_misurazioni()
        self.__lock = threading.Lock()

    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        with self.__lock:
            self.__listaMisurazioni.add_misurazione(timestamp, value, type_, latitude, longitude, ID_sensore, cella)

    def generate_new_health_score(self)->List[misurazione_salute]:
        health_scores = []
        with self.__lock:
            for cella in self.__listaMisurazioni.get_unique_celle():
                punteggio_cella = (
                    health_calculator.__calcola_incremento_tmp(cella, self.__listaMisurazioni) +
                    health_calculator.__calcola_incremento_umd(cella, self.__listaMisurazioni) +
                    health_calculator.__calcola_incremento_dst_PM10(cella, self.__listaMisurazioni)
                )
                health_scores.append(misurazione_salute(datetime.now(), punteggio_cella, self.__health_score_measure_type_naming, cella))
            self.__listaMisurazioni.clear_list()
            return health_scores

    @staticmethod
    def __calcola_incremento_tmp(cella: str, listaMisurazioni):
        return health_calculator.__tmpInc.get_incrementation(
            listaMisurazioni.get_list_by_cella_and_type(cella, health_calculator.__temperature_measure_type_naming))

    @staticmethod
    def __calcola_incremento_umd(cella: str, listaMisurazioni):
        return health_calculator.__umdInc.get_incrementation(
            listaMisurazioni.get_list_by_cella_and_type(cella, health_calculator.__humidity_measure_type_naming))

    @staticmethod
    def __calcola_incremento_dst_PM10(cella: str, listaMisurazioni):
        return health_calculator.__dstPm10Inc.get_incrementation(
            listaMisurazioni.get_list_by_cella_and_type(cella, health_calculator.__dtsPm10_measure_type_naming))
