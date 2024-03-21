from threading import Lock
from .writer import writer
from .writable import writable


class list_writer(writer):

    def __init__(self):
        self.__data_list = []
        self.__lock = Lock()  # Lock per garantire l'accesso thread-safe alla lista

    def write(self, to_write: writable) -> None:
        with self.__lock:
            self.__data_list.append(to_write)

    def get_data_list(self):
        with self.__lock:
            return self.__data_list
