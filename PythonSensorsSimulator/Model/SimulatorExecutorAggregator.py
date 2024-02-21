from .SimulatorExecutor import SimulatorExecutor
from .Writers.Writer import Writer
from .Simulators.TemperatureSimulator import TemperatureSimulator
from .Simulators.HumiditySimulator import HumiditySimulator
from .Simulators.ChargingStationSimulator import ChargingStationSimulator
from .Simulators.EcologicalIslandSimulator import EcologicalIslandSimulator
from .Simulators.WaterPresenceSensor import WaterPresenceSensor
from .SimulatorThread import SimulatorThread
from typing import List


class SimulatorExecutorAggregator:
    __simulator_executor: SimulatorExecutor = None

    def __init__(self):
        self.__simulator_executor = SimulatorExecutor()

    def add_temperature_simulator(
            self,
            writer: List[Writer],
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorAggregator":
        if writer is None:
            return self

        self.__simulator_executor.append_simulator(
            SimulatorThread(
                TemperatureSimulator(
                    writer, latitude, longitude,cella, frequency_in_s)
            )
        )
        return self
    
    def add_humidity_simulator(
            self,
            writer: List[Writer],
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorAggregator":
        if writer is None:
            return self

        self.__simulator_executor.append_simulator(
            SimulatorThread(
                HumiditySimulator(
                    writer, latitude, longitude,cella, frequency_in_s)
            )
        )
        return self
    
    def add_chargingStation_simulator(
            self,
            writer: List[Writer],
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorAggregator":
        if writer is None:
            return self

        self.__simulator_executor.append_simulator(
            SimulatorThread(
                ChargingStationSimulator(
                    writer, latitude, longitude,cella, frequency_in_s)
            )
        )
        return self
    
    def add_ecologicalIsland_simulator(
            self,
            writer: List[Writer],
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorAggregator":
        if writer is None:
            return self

        self.__simulator_executor.append_simulator(
            SimulatorThread(
                EcologicalIslandSimulator(
                    writer, latitude, longitude,cella, frequency_in_s)
            )
        )
        return self

    def add_waterPresence_simulator(
            self,
            writer: List[Writer],
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorAggregator":
        if writer is None:
            return self

        self.__simulator_executor.append_simulator(
            SimulatorThread(
                WaterPresenceSensor(
                    writer, latitude, longitude,cella, frequency_in_s)
            )
        )
        return self

    def get_simulator_executor(self) -> "SimulatorExecutor":
        sym_exec = self.__simulator_executor
        self.__simulator_executor = SimulatorExecutor()
        return sym_exec
