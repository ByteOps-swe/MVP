import threading
from .Writer import Writer
from .Writable import Writable

class StdoutWriter(Writer):

    def __init__(self):
        self.__lock = threading.Lock()

    def write(self, to_write: Writable) -> None:
        with self.__lock:
            print(to_write.to_json())
