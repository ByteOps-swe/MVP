from enum import Enum

class SensorTypes(Enum):
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    DUST_PM10 = "dust_pm10"
    CHARGING_STATION = "charging_station"
    ECOLOGICAL_ISLAND = "eco_zone"
    WATER_PRESENCE = "water_presence"
    ELECTRICAL_FAULT = "electricalFault"
