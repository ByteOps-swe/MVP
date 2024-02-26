
import threading
from .HealthCalculator import HealthCalculator

class HealthCalculatorThread(threading.Thread):
    __healthCalculator: HealthCalculator = None

    def __init__(self, healthCalculator: HealthCalculator):
        super().__init__()
        self.__healthCalculator = healthCalculator

    def run(self) -> None:
        self.__healthCalculator.run()

    def stop(self) -> None:
        self.__healthCalculator.stop()
