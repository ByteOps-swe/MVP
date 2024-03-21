from typing import List
from .component_simulator_thread import component_simulator_thread
from .ThreadPoolAdapter.thread_pool_target import thread_pool_target
#utilizzo di una THREADPOOL ADAPTER
#Pattern adapter

class simulator_thread_pool:

    def __init__(self, thread_pool_adapter: thread_pool_target):
        self.__simulators: List[component_simulator_thread] = []
        self.__thread_pool_adapter = thread_pool_adapter

    def run_all(self):
        self.__thread_pool_adapter.map(simulator_thread_pool.__start_simulator, self.__simulators)

    def stop_all(self):
        self.__thread_pool_adapter.map(simulator_thread_pool.__stop_simulator, self.__simulators)

    def append_simulator(self, simulator: component_simulator_thread):
        self.__simulators.append(simulator)

    @staticmethod
    def __start_simulator(simulator: component_simulator_thread):
        simulator.task()

    def __stop_simulator(self, simulator: component_simulator_thread):
        simulator.stop()
