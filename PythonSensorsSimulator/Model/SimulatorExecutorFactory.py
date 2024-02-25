from .SimulatorThreadPool import SimulatorThreadPool
from .Simulators.TemperatureSimulator import TemperatureSimulator
from .Simulators.HumiditySimulator import HumiditySimulator
from .Simulators.ChargingStationSimulator import ChargingStationSimulator
from .Simulators.EcologicalIslandSimulator import EcologicalIslandSimulator
from .Simulators.WaterPresenceSensor import WaterPresenceSensor
from .SimulatorThread import SimulatorThread
from .Writers.Writer import Writer
from .ThreadPoolAdapter.ThreadPoolExecutorAdapter import ThreadPoolExecutorAdapter
from .ComponentSimulatorThread import ComponentSimulatorThread


class SimulatorExecutorFactory(ComponentSimulatorThread):
    __simulator_executor: SimulatorThreadPool = None

    def __init__(self):
        self.__simulator_executor = SimulatorThreadPool(ThreadPoolExecutorAdapter())

    def add_temperature_simulator(
            self,
            writer: Writer,
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorFactory":
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
            writer: Writer,
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorFactory":
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
            writer: Writer,
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorFactory":
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
            writer: Writer,
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorFactory":
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
            writer: Writer,
            latitude: float,
            longitude: float,
            cella: str,
            frequency_in_s=1
    ) -> "SimulatorExecutorFactory":
        if writer is None:
            return self

        self.__simulator_executor.append_simulator(
            SimulatorThread(
                WaterPresenceSensor(
                    writer, latitude, longitude,cella, frequency_in_s)
            )
        )
        return self

    def run(self):
        self.__simulator_executor.run_all()
        
    def stop(self):
        self.__simulator_executor.stop_all()