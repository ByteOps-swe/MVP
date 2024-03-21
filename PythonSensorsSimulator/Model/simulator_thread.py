import time
from .Simulators import simulator
from .component_simulator_thread import component_simulator_thread
from .Writers.writer import writer
from .adapter_misurazione import adapter_misurazione

class simulator_thread(component_simulator_thread):

    def __init__(self, simulator: simulator, writers: writer, frequency: float = 10, data_to_generate: int = -1):
        super().__init__()
        self.__simulator = simulator
        self.__frequency = frequency
        self.__is_running = True
        self.__data_to_generate = data_to_generate
        self.__writers = writers

    def run(self) -> None:
        self.task()

    def task(self):
        last_measure = None
        while self.__is_running:
            if self.__data_to_generate == 0:
                self.stop()
                break
            if self.__data_to_generate > 0:
                self.__data_to_generate -= 1
            new_measure = self.__simulator.simulate()
            if last_measure is None or last_measure.get_value() != new_measure.get_value():
                self.__writers.write(adapter_misurazione(new_measure))
                last_measure = new_measure
            time.sleep(self.__frequency)

    def stop(self) -> None:
        self.__is_running = False
