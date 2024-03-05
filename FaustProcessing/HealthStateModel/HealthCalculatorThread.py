import threading
import time
from .HealthAlgorithm import HealthAlgorithm
from .Writers.Writer import Writer
from .AdapterMisurazioneSalute import AdapterMisurazione

class HealthCalculatorThread(threading.Thread):
    """
    A thread class for calculating and generating health scores.

    Args:
        healthCalculator (HealthCalculator): An instance of the HealthCalculator class.
        writers (Writer): An instance of the Writer class.
        frequency (float, optional): The frequency at which health scores are generated. Defaults to 10.
        data_to_generate (int, optional): The number of data points to generate. Defaults to -1, which means infinite.

    Attributes:
        __healthCalculator (HealthCalculator): An instance of the HealthCalculator class.
        __frequency (float): The frequency at which health scores are generated.
        __is_running (bool): Flag indicating whether the thread is running.
        __data_to_generate (int): The number of data points to generate.
        __writers (Writer): An instance of the Writer class.

    Methods:
        run(): The main method that runs the thread.
        stop(): Stops the thread.

    """
    def __init__(self, healthCalculator: HealthAlgorithm, writers: Writer, frequency:float = 10, data_to_generate:int = -1 ):
        super().__init__()
        self.__healthCalculator = healthCalculator
        self.__frequency = frequency
        self.__is_running = True
        self.__data_to_generate = data_to_generate
        self.__writers = writers

    def run(self) -> None:
        """
        The main method that runs the thread.

        This method generates health scores using the health calculator and writes them using the writers.
        The thread continues running until the stop method is called or the specified number of data points is generated.

        """
        while self.__is_running:
            if self.__data_to_generate != -1:
                if self.__data_to_generate <= 0:
                    self.stop()
                else:
                    self.__data_to_generate -= 1
            health_scores = self.__healthCalculator.generate_new_health_score()
            for element in health_scores:
                self.__writers.write(AdapterMisurazione(element))
            time.sleep(self.__frequency)

    def stop(self) -> None:
        """
        Stops the thread.

        This method sets the is_running flag to False, which stops the execution of the thread.

        """
        self.__is_running = False
