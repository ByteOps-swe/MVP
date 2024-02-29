from .ListaMisurazioni import ListaMisurazioni
from .MisurazioneSalute import MisurazioneSalute
from .Incrementers.TemperatureIncrementer import TemperatureIncrementer
from .Incrementers.HumidityIncrementer import HumidityIncrementer
from datetime import datetime
import threading

class HealthCalculator():
    __tmpInc = TemperatureIncrementer()
    __umdInc = HumidityIncrementer()

    def __init__(self, temperature_measure_type_naming:str="temperature",humidity_measure_type_naming:str="humidity", healthScore_measure_type_naming:str="PunteggioSalute"):
        self.__listaMisurazioni = ListaMisurazioni()
        self.__temperature_measure_type_naming = temperature_measure_type_naming
        self.__humidity_measure_type_naming = humidity_measure_type_naming
        self.__healthScore_measure_type_naming = healthScore_measure_type_naming
        self.__lock = threading.Lock()  

    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        with self.__lock:  
            self.__listaMisurazioni.add_misurazione(timestamp, value, type_, latitude, longitude, ID_sensore, cella)
    
    def generate_new_health_score(self):
        health_scores = []
        with self.__lock:  
            for cella in self.__listaMisurazioni.get_unique_celle():
                punteggio_cella = HealthCalculator.__calcola_incremento_tmp(cella,self.__listaMisurazioni,self.__temperature_measure_type_naming) + HealthCalculator.__calcola_incremento_umd(cella,self.__listaMisurazioni,self.__humidity_measure_type_naming)
                health_scores.append(MisurazioneSalute(datetime.now(), punteggio_cella, self.__healthScore_measure_type_naming, cella))
            self.__listaMisurazioni.clear_list()
            return health_scores

    def __calcola_incremento_tmp(cella:str,listaMisurazioni,temperature_measure_type_naming):
        return HealthCalculator.__tmpInc.get_incrementation(listaMisurazioni.get_list_by_cella_and_type(cella, temperature_measure_type_naming))
    
    def __calcola_incremento_umd(cella:str,listaMisurazioni,humidity_measure_type_naming):
        return HealthCalculator.__umdInc.get_incrementation(listaMisurazioni.get_list_by_cella_and_type(cella,humidity_measure_type_naming))
