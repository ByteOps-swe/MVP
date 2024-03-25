import threading
from .writer_strategy import writer_strategy
from .writable import writable

class std_out_writer(writer_strategy):

    def __init__(self):
        self.__lock = threading.Lock()

    def write(self, to_write: writable) -> None:
        with self.__lock:
            print(to_write.to_json())
