from .Writer import Writer
from threading import Lock
from .Writable import Writable


class ListWriter(Writer):
    def __init__(self):
        self.__data_list = []
        self.__lock = Lock()  # Lock per garantire l'accesso thread-safe alla lista

    def write(self, to_write: Writable) -> None:
        with self.__lock: 
            self.__data_list.append(to_write)

    def get_data_list(self) -> list:
        with self.__lock:  # Acquisisce il lock prima di ottenere la lista
            return self.__data_list