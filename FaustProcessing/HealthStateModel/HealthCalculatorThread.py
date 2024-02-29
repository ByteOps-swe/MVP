
import threading
from .HealthCalculator import HealthCalculator
from .Writers import Writer
from .AdapterMisurazioneSalute import AdapterMisurazione
import time 
class HealthCalculatorThread(threading.Thread):
    __healthCalculator: HealthCalculator = None

    def __init__(self, healthCalculator: HealthCalculator, writers: Writer, frequency:float = 10, data_to_generate:int = None ):
        super().__init__()
        self.__healthCalculator = healthCalculator
        self.__frequency = frequency
        self.__is_running = True
        self.__data_to_generate = data_to_generate
        self.__writers = writers

    def run(self) -> None:
        while self.__is_running:
            if self.__data_to_generate is not None:
                if self.__data_to_generate <= 0:
                    self.stop()
                else:
                    self.__data_to_generate -= 1 
            health_scores = self.__healthCalculator.generate_new_health_score()
            [self.__writers.write(AdapterMisurazione(element)) for element in health_scores]
            time.sleep(self.__frequency)

    def stop(self) -> None:
        self.__is_running = False
