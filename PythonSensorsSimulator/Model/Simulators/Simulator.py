from abc import ABC, abstractmethod
from ..Writers import Writer


class Simulator(ABC):
    writer: Writer
    frequency: int
    is_simulating: bool
    ID_sensor: str
    cella_sensore: str
    latitude: float
    longitude: float

    def __init__(self, writer: Writer, latitude: float, longitude: float, cella: str, sensor_id: str, frequency_in_s: int = 10):
        self.writer = writer
        self.frequency = frequency_in_s
        self.is_simulating = True
        self.ID_sensor = sensor_id
        self.cella_sensore = cella
        self.latitude = latitude
        self.longitude = longitude

    @abstractmethod
    def simulate(self) -> None:
        pass

    @abstractmethod
    def generate_measure(self) -> None:
        pass

    def stop_simulating(self) -> None:
        self.is_simulating = False

    def isSimulating(self) -> bool: #Sta ancora simulando?
        return self.is_simulating
