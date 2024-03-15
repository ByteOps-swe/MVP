from .temperature_simulator import temperature_simulator
from .humidity_simulator import humidity_simulator
from .charging_station_simulator import charging_station_simulator
from .ecological_island_simulator import ecological_island_simulator
from .water_presence_sensor import water_presence_sensor
from .electrical_fault_simulator import electrical_fault_simulator
from .dust_PM10_simulator import dust_PM10_simulator

class sensor_factory:
    @staticmethod
    def create_temperature_sensor(latitude: float, longitude: float, cella: str = "Centro", initial_value=20):
        return temperature_simulator(latitude, longitude, cella, initial_value)

    @staticmethod
    def create_humidity_sensor(latitude: float, longitude: float, cella: str = "Centro", initial_value=50):
        return humidity_simulator(latitude, longitude, cella, initial_value)

    @staticmethod
    def create_charging_station_sensor(latitude: float, longitude: float, cella: str = "Centro", probabilita_occupazione=0.5):
        return charging_station_simulator(latitude, longitude, cella, probabilita_occupazione)

    @staticmethod
    def create_ecological_island_sensor(latitude: float, longitude: float, cella: str = "Centro", initial_value=50):
        return ecological_island_simulator(latitude, longitude, cella, initial_value)

    @staticmethod
    def create_water_presence_sensor(latitude: float, longitude: float, cella: str = "Centro", soglia_rilevamento=0.5):
        return water_presence_sensor(latitude, longitude, cella, soglia_rilevamento)

    @staticmethod
    def create_dust_PM10_sensor(latitude: float, longitude: float, cella: str = "Centro", initial_value=20):
        return dust_PM10_simulator(latitude, longitude, cella, initial_value)

    @staticmethod
    def create_eletrical_fault_sensor(latitude: float, longitude: float, cella: str = "Centro", fault_probability=0.5):
        return electrical_fault_simulator(latitude, longitude, cella, fault_probability)
