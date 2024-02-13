import threading

from .Simulators.Simulator import Simulator


class SimulatorThread(threading.Thread):
    __simulator: Simulator = None

    def __init__(self, simulator: Simulator):
        super().__init__()
        self.__simulator = simulator

    def run(self) -> None:
        self.__simulator.simulate()

    def stop(self) -> None:
        self.__simulator.stop_simulating()
