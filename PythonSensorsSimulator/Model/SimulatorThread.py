import time
from .Simulators.Simulator import Simulator
from .ComponentSimulatorThread import ComponentSimulatorThread
from .Writers.Writer import Writer
from .AdapterMisurazione import AdapterMisurazione

class SimulatorThread(ComponentSimulatorThread):

    def __init__(self, simulator: Simulator, writers: Writer, frequency: float = 10, data_to_generate: int = -1):
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
            elif self.__data_to_generate > 0:
                self.__data_to_generate -= 1
            new_measure = self.__simulator.simulate()
            if last_measure is None or last_measure.get_value() != new_measure.get_value():
                #faccio in modo che venga inviato il dato solo se è differente dal precedente,
                #altrimenti non ha senso
                self.__writers.write(AdapterMisurazione(new_measure))
                last_measure = new_measure
            time.sleep(self.__frequency)

    def stop(self) -> None:
        self.__is_running = False
