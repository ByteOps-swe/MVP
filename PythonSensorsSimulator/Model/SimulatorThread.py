from .Simulators.Simulator import Simulator
from .ComponentSimulatorThread import ComponentSimulatorThread


class SimulatorThread(ComponentSimulatorThread):
    __simulator: Simulator = None

    def __init__(self, simulator: Simulator):
        super().__init__()
        self.__simulator = simulator

    def run(self) -> None:
        self.__simulator.simulate()

    def stop(self) -> None:
        self.__simulator.stop_simulating()
