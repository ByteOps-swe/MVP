from .ComponentSimulatorThread import ComponentSimulatorThread
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
        self.__thread_pool_adapter.map(self.__stop_simulator, self.__simulators)

    def append_simulator(self, simulator: ComponentSimulatorThread):
        self.__simulators.append(simulator)

    def __start_simulator(self, simulator: ComponentSimulatorThread):
        simulator.start()
    
    def __stop_simulator(self, simulator: ComponentSimulatorThread):
        simulator.stop()