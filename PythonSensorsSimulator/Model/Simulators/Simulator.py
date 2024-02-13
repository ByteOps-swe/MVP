from abc import ABC, abstractmethod
from ..Writers import Writer


class Simulator(ABC):
    _writer: Writer
    _frequency_in_s: int
    __continue_simulating: bool
    _sensor_name: str
    _latitude: float
    _longitude: float

    def __init__(self, writer: Writer, latitude: float, longitude: float, sensor_name: str, frequency_in_s: int = 10):
        self._writer = writer
        self._frequency_in_s = frequency_in_s
        self.__continue_simulating = True
        self._sensor_name = sensor_name
        self._latitude = latitude
        self._longitude = longitude

    @abstractmethod
    def simulate(self) -> None:
        pass

    @abstractmethod
    def generate_measure(self) -> None:
        pass

    def stop_simulating(self) -> None:
        self.__continue_simulating = False

    def continue_simulating(self) -> bool:
        return self.__continue_simulating
