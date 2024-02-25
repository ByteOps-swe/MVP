from .TemperatureSimulator import TemperatureSimulator
from .HumiditySimulator import HumiditySimulator
from .ChargingStationSimulator import ChargingStationSimulator
from .EcologicalIslandSimulator import EcologicalIslandSimulator
from .WaterPresenceSensor import WaterPresenceSensor
from ..Writers.Writer import Writer

class SensorFactory:
    @staticmethod
    def create_temperature_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_value=20):
        return TemperatureSimulator(writer, latitude, longitude, cella, frequency_in_s, initial_value)

    @staticmethod
    def create_humidity_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_value=20):
        return HumiditySimulator(writer, latitude, longitude, cella, frequency_in_s, initial_value)

    @staticmethod
    def create_charging_station_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_value=20):
        return ChargingStationSimulator(writer, latitude, longitude, cella, frequency_in_s, initial_value)

    @staticmethod
    def create_ecological_island_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_value=20):
        return EcologicalIslandSimulator(writer, latitude, longitude, cella, frequency_in_s, initial_value)

    @staticmethod
    def create_water_presence_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_value=20):
        return WaterPresenceSensor(writer, latitude, longitude, cella, frequency_in_s, initial_value)

