from typing import List
from .ComponentSimulatorThread import ComponentSimulatorThread
from .ThreadPoolAdapter.ThreadPoolTarget import ThreadPoolTarget
#utilizzo di una THREADPOOL ADAPTER
#Pattern adapter

class SimulatorThreadPool:
    """
    A class representing a thread pool for running component simulators.

    Attributes:
        __simulators (List[ComponentSimulatorThread]): A list of component simulator threads.
        __thread_pool_adapter (ThreadPoolTarget): An adapter for the thread pool implementation.

    Methods:
        run_all(): Runs all the component simulators in the thread pool.
        stop_all(): Stops all the component simulators in the thread pool.
        append_simulator(simulator: ComponentSimulatorThread): Appends a component simulator to the thread pool.
    """

    def __init__(self, thread_pool_adapter: ThreadPoolTarget):
        self.__simulators: List[ComponentSimulatorThread] = []
        self.__thread_pool_adapter = thread_pool_adapter

    def run_all(self):
        """Runs all the component simulators in the thread pool."""
        self.__thread_pool_adapter.map(self.__start_simulator, self.__simulators)

    def stop_all(self):
        """Stops all the component simulators in the thread pool."""
        self.__thread_pool_adapter.map(self.__stop_simulator, self.__simulators)

    def append_simulator(self, simulator: ComponentSimulatorThread):
        """
        Appends a component simulator to the thread pool.

        Args:
            simulator (ComponentSimulatorThread): The component simulator thread to be appended.
        """
        self.__simulators.append(simulator)

    def __start_simulator(self, simulator: ComponentSimulatorThread):
        """
        Starts a component simulator.

        Args:
            simulator (ComponentSimulatorThread): The component simulator thread to be started.
        """
        simulator.start()

    def __stop_simulator(self, simulator: ComponentSimulatorThread):
        """
        Stops a component simulator.

        Args:
            simulator (ComponentSimulatorThread): The component simulator thread to be stopped.
        """
        simulator.stop()
