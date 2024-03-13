from typing import List
from .ComponentSimulatorThread import ComponentSimulatorThread
from .ThreadPoolAdapter.ThreadPoolTarget import ThreadPoolTarget
#utilizzo di una THREADPOOL ADAPTER
#Pattern adapter

class SimulatorThreadPool:

    def __init__(self, thread_pool_adapter: ThreadPoolTarget):
        self.__simulators: List[ComponentSimulatorThread] = []
        self.__thread_pool_adapter = thread_pool_adapter

    def run_all(self):
        self.__thread_pool_adapter.map(SimulatorThreadPool.__start_simulator, self.__simulators)

    def stop_all(self):
        self.__thread_pool_adapter.map(SimulatorThreadPool.__stop_simulator, self.__simulators)

    def append_simulator(self, simulator: ComponentSimulatorThread):
        self.__simulators.append(simulator)

    @staticmethod
    def __start_simulator(simulator: ComponentSimulatorThread):
        simulator.task()
    @staticmethod
    def __stop_simulator(simulator: ComponentSimulatorThread):
        simulator.stop()
