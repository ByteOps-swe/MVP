import threading
import time
from .HealthAlgorithm import HealthAlgorithm
from .Writers.Writer import Writer
from .AdapterMisurazioneSalute import AdapterMisurazione

class HealthCalculatorThread(threading.Thread):
    def __init__(self, healthCalculator: HealthAlgorithm, writers: Writer, frequency:float = 10, data_to_generate:int = -1 ):
        super().__init__()
        self.__healthCalculator = healthCalculator
        self.__frequency = frequency
        self.__is_running = True
        self.__data_to_generate = data_to_generate
        self.__writers = writers

    def run(self) -> None:
        while self.__is_running:
            if self.__data_to_generate == 0:
                self.stop()
            elif self.__data_to_generate > 0:
                self.__data_to_generate -= 1
            health_scores = self.__healthCalculator.generate_new_health_score()
            for element in health_scores:
                self.__writers.write(AdapterMisurazione(element))
            time.sleep(self.__frequency)

    def stop(self) -> None:
        self.__is_running = False
