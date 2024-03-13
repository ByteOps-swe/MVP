from abc import ABC
import threading
from .ListaMisurazioni import ListaMisurazioni


#Pattern Strategy
class HealthProcessorBuffer(ABC):

    def __init__(self):
        self.__listaMisurazioni = ListaMisurazioni()
        self.__lock = threading.Lock()

    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        with self.__lock:
            self.__listaMisurazioni.add_misurazione(timestamp, value, type_, latitude, longitude, ID_sensore, cella)

    def get_lista_misurazioni(self):
        return self.__listaMisurazioni

    def clear_list(self):
        self.__listaMisurazioni.clear_list()
