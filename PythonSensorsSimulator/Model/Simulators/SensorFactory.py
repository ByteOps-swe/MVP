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
    def create_humidity_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_value=50):
        return HumiditySimulator(writer, latitude, longitude, cella, frequency_in_s, initial_value)

    @staticmethod
    def create_charging_station_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, probabilita_occupazione=0.5):
        return ChargingStationSimulator(writer, latitude, longitude, cella, frequency_in_s, probabilita_occupazione)

    @staticmethod
    def create_ecological_island_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_value=50):
        return EcologicalIslandSimulator(writer, latitude, longitude, cella, frequency_in_s, initial_value)

    @staticmethod
    def create_water_presence_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, soglia_rilevamento=0.5):
        return WaterPresenceSensor(writer, latitude, longitude, cella, frequency_in_s, soglia_rilevamento)

    @staticmethod
    def create_dust_PM10_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_value=20):
        return WaterPresenceSensor(writer, latitude, longitude, cella, frequency_in_s, initial_value)

    @staticmethod
    def create_eletrical_fault_sensor(writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, fault_probability=0.5):
        return WaterPresenceSensor(writer, latitude, longitude, cella, frequency_in_s, fault_probability)

