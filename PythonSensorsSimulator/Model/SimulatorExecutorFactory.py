from .Simulators.Simulator import Simulator
from .SimulatorThreadPool import SimulatorThreadPool
from .SimulatorThread import SimulatorThread
from .ThreadPoolAdapter.ThreadPoolExecutorAdapter import ThreadPoolExecutorAdapter
from .ComponentSimulatorThread import ComponentSimulatorThread
from .Writers.Writer import Writer

class SimulatorExecutorFactory(ComponentSimulatorThread):
    def __init__(self):
        self.__simulator_executor = SimulatorThreadPool(ThreadPoolExecutorAdapter())

    def add_simulator(self, simulator: Simulator, writers: Writer, frequency:float = 10, data_to_generate:int = None) -> "SimulatorExecutorFactory":
        self.__simulator_executor.append_simulator(SimulatorThread(simulator ,writers,frequency, data_to_generate))
        return self
    
    def add_simulator_thread(self, thread_simulator : ComponentSimulatorThread) -> "SimulatorExecutorFactory":
        self.__simulator_executor.append_simulator(thread_simulator)
        return self

    def run(self):
        self.__simulator_executor.run_all()

    def stop(self):
        self.__simulator_executor.stop_all()
