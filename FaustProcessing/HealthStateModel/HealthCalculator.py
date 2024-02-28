from .ListaMisurazioni import ListaMisurazioni
from .MisurazioneSalute import MisurazioneSalute
from .Incrementers.TemperatureIncrementer import TemperatureIncrementer
from .Incrementers.HumidityIncrementer import HumidityIncrementer

from  .Writers.Writer import Writer
from datetime import datetime
import time
import threading

class HealthCalculator():

    def __init__(self, writer: Writer, temperature_measure_type_naming:str="temperature",humidity_measure_type_naming:str="humidity", healthScore_measure_type_naming:str="PunteggioSalute", frequency:int=10):
        self.__listaMisurazioni = ListaMisurazioni()
        self.__tmpInc = TemperatureIncrementer()
        self.__umdInc = HumidityIncrementer()
        self.__writers = writer
        self.__is_running = True
        self.__frequency = frequency
        self.__temperature_measure_type_naming = temperature_measure_type_naming
        self.__humidity_measure_type_naming = humidity_measure_type_naming
        self.__healthScore_measure_type_naming = healthScore_measure_type_naming
        self.__lock = threading.Lock()  # Lock per sincronizzare l'accesso alla lista

    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        with self.__lock:  # Acquisizione del lock prima dell'accesso alla lista
            self.__listaMisurazioni.add_misurazione(timestamp, value, type_, latitude, longitude, ID_sensore, cella)
    
    def generate_new_health_score(self):
        with self.__lock:  # Acquisizione del lock prima dell'accesso alla lista
            for cella in self.__listaMisurazioni.get_unique_celle():
                punteggio_cella = self.__calcola_incremento_tmp(cella) + self.__calcola_incremento_umd(cella)
                self.__writers.write(MisurazioneSalute(datetime.now(), punteggio_cella, self.__healthScore_measure_type_naming, cella))
            self.__listaMisurazioni.clear_list()

    def __calcola_incremento_tmp(self,cella:str):
        return self.__tmpInc.get_incrementation(self.__listaMisurazioni.get_list_by_cella_and_type(cella, self.__temperature_measure_type_naming))
    
    def __calcola_incremento_umd(self,cella:str):
        return self.__umdInc.get_incrementation(self.__listaMisurazioni.get_list_by_cella_and_type(cella, self.__humidity_measure_type_naming))

    def run(self) -> None:
        while self.__is_running:
            self.generate_new_health_score()
            time.sleep(self.__frequency)

    def stop(self) -> None:
        self.__is_running = False