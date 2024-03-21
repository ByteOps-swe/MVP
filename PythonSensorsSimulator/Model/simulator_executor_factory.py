from .Simulators import simulator
from .simulator_thread_pool import simulator_thread_pool
from .simulator_thread import simulator_thread
from .ThreadPoolAdapter.thread_pool_executor_adapter import thread_pool_executor_adapter
from .component_simulator_thread import component_simulator_thread
from .Writers.writer import writer

class simulator_executor_factory(component_simulator_thread):
    def __init__(self):
        super().__init__()
        self.__simulator_executor = simulator_thread_pool(thread_pool_executor_adapter(20))

    def add_simulator(self, simulator: simulator, writers: writer, frequency:float = 10, data_to_generate:int = -1) -> "simulator_executor_factory":
        self.__simulator_executor.append_simulator(simulator_thread(simulator ,writers,frequency, data_to_generate))
        return self

    def add_simulator_thread(self, thread_simulator : component_simulator_thread) -> "simulator_executor_factory":
        self.__simulator_executor.append_simulator(thread_simulator)
        return self

    def run(self):
        self.__simulator_executor.run_all()

    def stop(self):
        self.__simulator_executor.stop_all()

    def task(self):
        self.__simulator_executor.run_all()
