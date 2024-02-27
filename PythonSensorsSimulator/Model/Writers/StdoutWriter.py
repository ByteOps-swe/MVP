from .Writer import Writer
from .Writable import Writable
import threading

class StdoutWriter(Writer):
    __counter_lock = threading.Lock()
    __message_counter = 0
    
    def __init__(self):
        self.__lock = threading.Lock()
        
    def write(self, to_write: Writable) -> None:
        with self.__lock:
            print(to_write.to_json())
            self.__update_counter()
            
    @classmethod
    def __update_counter(cls):
        with cls.__counter_lock:
            cls.__message_counter += 1
            print(f"Total messages printed: {cls.__message_counter}")
