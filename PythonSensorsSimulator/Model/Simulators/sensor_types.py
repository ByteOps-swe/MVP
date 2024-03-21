from enum import Enum

class sensor_types(Enum):
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    DUST_PM10 = "dust_PM10"
    CHARGING_STATION = "charging_station"
    ECOLOGICAL_ISLAND = "eco_zone"
    WATER_PRESENCE = "water_presence"
    ELECTRICAL_FAULT = "electricalFault"
