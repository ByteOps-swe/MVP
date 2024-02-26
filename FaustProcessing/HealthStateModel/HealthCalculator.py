from .ListaMisurazioni import ListaMisurazioni
from .MisurazioneSalute import MisurazioneSalute
from .Incrementers.TemperatureIncrementer import TemperatureIncrementer
from  .Writers.Writer import Writer
from datetime import datetime
import time

class HealthCalculator():

    def __init__(self,writer: Writer, temperature_measure_type_naming = "temperature", healthScore_measure_type_naming = "PunteggioSalute", frequency = 10):
        self.__listaMisurazioni = ListaMisurazioni()
        self.__tmpInc = TemperatureIncrementer()
        self.__writers = writer
        self.__is_running = True
        self.__frequency = frequency
        self.__temperature_measure_type_naming = temperature_measure_type_naming
        self.__healthScore_measure_type_naming = healthScore_measure_type_naming

    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        self.__listaMisurazioni.add_misurazione(timestamp, value, type_, latitude, longitude, ID_sensore, cella)
    
    def generate_new_health_score(self):
        for cella in self.__listaMisurazioni.get_unique_celle():
            punteggio_cella = self.__tmpInc.get_incrementation(self.__listaMisurazioni.get_list_by_cella_and_type(cella,HealthCalculator.temperature_measure_type_naming)) 
            self.__writers.write(MisurazioneSalute(datetime.now(), punteggio_cella , self.__healthScore_measure_type_naming, cella))
            self.__listaMisurazioni.clear_list()
    
    def run(self) -> None:
        while self.__is_running:
            self.generate_new_health_score()
            time.sleep(self.__frequency)

    def stop(self) -> None:
        self.__is_running = False
    
    def get_temperature_measure_type_naming(self):
        return self.__temperature_measure_type_naming


    
