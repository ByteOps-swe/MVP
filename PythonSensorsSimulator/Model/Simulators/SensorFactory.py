from .TemperatureSimulator import TemperatureSimulator
from .HumiditySimulator import HumiditySimulator
from .ChargingStationSimulator import ChargingStationSimulator
from .EcologicalIslandSimulator import EcologicalIslandSimulator
from .WaterPresenceSensor import WaterPresenceSensor
from .ElectricalFaultSimulator import ElectricalFaultSimulator
from .DustPM10Simulator import DustPM10Simulator

class SensorFactory:
    @staticmethod
    def create_temperature_sensor(latitude: float, longitude: float, cella: str = "Centro", initial_value=20):
        return TemperatureSimulator(latitude, longitude, cella, initial_value)

    @staticmethod
    def create_humidity_sensor(latitude: float, longitude: float, cella: str = "Centro", initial_value=50):
        return HumiditySimulator(latitude, longitude, cella, initial_value)

    @staticmethod
    def create_charging_station_sensor(latitude: float, longitude: float, cella: str = "Centro", probabilita_occupazione=0.5):
        return ChargingStationSimulator(latitude, longitude, cella, probabilita_occupazione)

    @staticmethod
    def create_ecological_island_sensor(latitude: float, longitude: float, cella: str = "Centro", initial_value=50):
        return EcologicalIslandSimulator(latitude, longitude, cella, initial_value)

    @staticmethod
    def create_water_presence_sensor(latitude: float, longitude: float, cella: str = "Centro", soglia_rilevamento=0.5):
        return WaterPresenceSensor(latitude, longitude, cella, soglia_rilevamento)

    @staticmethod
    def create_dust_PM10_sensor(latitude: float, longitude: float, cella: str = "Centro", initial_value=20):
        return DustPM10Simulator(latitude, longitude, cella, initial_value)

    @staticmethod
    def create_eletrical_fault_sensor(latitude: float, longitude: float, cella: str = "Centro", fault_probability=0.5):
        return ElectricalFaultSimulator(latitude, longitude, cella, fault_probability)

