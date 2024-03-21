import threading
import time
from .health_algorithm import health_algorithm
from .Writers import writer
from .adapter_misurazione_salute import adapter_misurazione

class health_calculator_thread(threading.Thread):
    def __init__(self, health_calculator: health_algorithm, writers: writer, frequency:float = 10, data_to_generate:int = -1 ):
        super().__init__()
        self.__health_calculator = health_calculator
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
            health_scores = self.__health_calculator.generate_new_health_score()
            for element in health_scores:
                self.__writers.write(adapter_misurazione(element))
            time.sleep(self.__frequency)

    def stop(self) -> None:
        self.__is_running = False
