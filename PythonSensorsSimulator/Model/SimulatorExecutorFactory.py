from .Simulators.Simulator import Simulator
from .SimulatorThreadPool import SimulatorThreadPool
from .SimulatorThread import SimulatorThread
from .ThreadPoolAdapter.ThreadPoolExecutorAdapter import ThreadPoolExecutorAdapter
from .ComponentSimulatorThread import ComponentSimulatorThread

class SimulatorExecutorFactory(ComponentSimulatorThread):
    def __init__(self):
        self.__simulator_executor = SimulatorThreadPool(ThreadPoolExecutorAdapter())

    def add_simulator(self, simulator: Simulator) -> "SimulatorExecutorFactory":
        self.__simulator_executor.append_simulator(SimulatorThread(simulator))
        return self

    def run(self):
        self.__simulator_executor.run_all()

    def stop(self):
        self.__simulator_executor.stop_all()
