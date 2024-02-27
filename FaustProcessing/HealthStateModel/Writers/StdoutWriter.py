from .Writer import Writer
from ..MisurazioneSalute import MisurazioneSalute
import threading

class StdoutWriter(Writer):
 
    def __init__(self):
        self.__lock = threading.Lock()
        
    def write(self, to_write: MisurazioneSalute) -> None:
        with self.__lock:
            print(to_write.to_json())
