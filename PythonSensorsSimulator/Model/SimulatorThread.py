import time
from .Simulators.Simulator import Simulator
from .ComponentSimulatorThread import ComponentSimulatorThread
from .Writers.Writer import Writer
from .AdapterMisurazione import AdapterMisurazione

class SimulatorThread(ComponentSimulatorThread):
    """
    A class representing a simulator thread.

    This class extends the ComponentSimulatorThread class and provides functionality
    to simulate data generation at a specified frequency.

    Attributes:
        __simulator (Simulator): The simulator object used for data generation.
        __frequency (float): The frequency at which data is generated.
        __is_running (bool): Flag indicating whether the thread is running or not.
        __data_to_generate (int): The number of data points to generate (-1 for infinite).
        __writers (Writer): The writer object used to write the generated data.

    Methods:
        run(): Starts the data generation process.
        stop(): Stops the data generation process.
    """

    def __init__(self, simulator: Simulator, writers: Writer, frequency: float = 10, data_to_generate: int = -1):
        super().__init__()
        self.__simulator = simulator
        self.__frequency = frequency
        self.__is_running = True
        self.__data_to_generate = data_to_generate
        self.__writers = writers

    def run(self) -> None:
        """
        Starts the data generation process.

        This method runs in a loop, generating data at the specified frequency
        until the specified number of data points is generated or the stop() method
        is called.
        """
        while self.__is_running:
            if self.__data_to_generate != -1:
                if self.__data_to_generate <= 0:
                    self.stop()
                else:
                    self.__data_to_generate -= 1
            self.__writers.write(AdapterMisurazione(self.__simulator.simulate()))
            time.sleep(self.__frequency)

    def stop(self) -> None:
        """
        Stops the data generation process.

        This method sets the __is_running flag to False, causing the run() method
        to exit the loop and stop the data generation process.
        """
        self.__is_running = False
