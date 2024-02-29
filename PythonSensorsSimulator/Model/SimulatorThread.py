from .Simulators.Simulator import Simulator
from .ComponentSimulatorThread import ComponentSimulatorThread
from .Writers.Writer import Writer
from .AdapterMisurazione import AdapterMisurazione
import time

class SimulatorThread(ComponentSimulatorThread):
    def __init__(self, simulator: Simulator, writers: Writer, frequency:float = 10, data_to_generate:int = None):
        super().__init__()
        self.__simulator = simulator
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
            self.__writers.write(AdapterMisurazione(self.__simulator.simulate()))
            time.sleep(self.__frequency)

    def stop(self) -> None:
        self.__is_running = False
