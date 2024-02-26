from .ListaMisurazioni import ListaMisurazioni
from .Misurazione import Misurazione
from .MisurazioneSalute import MisurazioneSalute
from .Incrementers.TemperatureIncrementer import TemperatureIncrementer
from  .Writers.Writer import Writer
import time
from datetime import datetime

class HealthCalculator():
    temperature_topic ="temperature"

    def __init__(self,writer: Writer):
        self.__listaMisurazioni = ListaMisurazioni()
        self.__tmpInc = TemperatureIncrementer()
        self.__writers = writer


    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        self.__listaMisurazioni.add_misurazione(timestamp, value, type_, latitude, longitude, ID_sensore, cella)
    
    def generate_new_health_score(self):
        for cella in self.__listaMisurazioni.get_unique_celle():
            punteggio_cella = self.__tmpInc.get_incrementation(self.__listaMisurazioni.get_list_by_cella_and_type(cella,HealthCalculator.temperature_topic)) 
            self.__writers.write(MisurazioneSalute(datetime.now(), punteggio_cella , "PunteggioSalute",cella))
            self.__listaMisurazioni.clear_list()


    
