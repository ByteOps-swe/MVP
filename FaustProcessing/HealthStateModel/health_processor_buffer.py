from abc import ABC
import threading
from .lista_misurazioni import lista_misurazioni

#Pattern Strategy
class health_processor_buffer(ABC):

    def __init__(self):
        self.__lista_misurazioni = lista_misurazioni()
        self.__lock = threading.Lock()

    def add_misurazione(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        with self.__lock:
            self.__lista_misurazioni.add_misurazione(timestamp, value, type_, latitude, longitude, ID_sensore, cella)

    def get_lista_misurazioni(self):
        return self.__lista_misurazioni

    def clear_list(self):
        self.__lista_misurazioni.clear_list()
