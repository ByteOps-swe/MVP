from .SimulatorThread import SimulatorThread


class SimulatorExecutor:
    __simulators: [SimulatorThread] = []

    def __init__(self):
        pass

    def run_all(self) -> None:
        for simulator in self.__simulators:
            simulator.start()

    def stop_all(self) -> None:
        for simulator in self.__simulators:
            simulator.stop()

    def append_simulator(self, simulator_thread: SimulatorThread) -> None:
        self.__simulators.append(simulator_thread)
