import concurrent.futures
from .Simulators.Simulator import Simulator
from .ThreadPoolAdapter.ThreadPoolTarget import ThreadPoolTarget

#utilizzo di una THREADPOOL ADAPTER
#Pattern adapter

class SimulatorThreadPool:
    def __init__(self, thread_pool_adapter: ThreadPoolTarget):
        self.__simulators = []
        self.__thread_pool_adapter = thread_pool_adapter

    def run_all(self):
        self.__thread_pool_adapter.map(self.__start_simulator, self.__simulators)

    def stop_all(self):
        for simulator in self.__simulators:
            simulator.stop()

    def append_simulator(self, simulator):
        self.__simulators.append(simulator)

    def __start_simulator(self, simulator):
        simulator.start()