from datetime import datetime
from .coordinate import coordinate

class misurazione():
    def __init__(self, timestamp: datetime, value, type_: str, coord: coordinate, ID_sensore: str, cella: str):
        self.__timestamp = timestamp
        self.__value = value
        self.__type = type_
        self.__coordinates = coord
        self.__ID_sensore = ID_sensore
        self.__cella = cella

    def get_timestamp(self):
        return self.__timestamp

    def get_value(self):
        return self.__value

    def get_type(self):
        return self.__type

    def get_latitude(self):
        return self.__coordinates.get_latitude()

    def get_longitude(self):
        return self.__coordinates.get_longitude()

    def get_ID_sensore(self):
        return self.__ID_sensore

    def get_cella(self):
        return self.__cella

    def to_string(self):
        return f"Timestamp: {self.__timestamp.replace(microsecond=0)}, Value: {round(self.__value,2)}, Type: {self.__type}, Coordinates: {self.__coordinates.get_latitude()},{self.__coordinates.get_longitude()}, Sensor ID: {self.__ID_sensore}, Cell: {self.__cella}"

    def __eq__(self, other):
        if not isinstance(other, misurazione):
            return False
        return (
            str(self.__timestamp) == str(other.__timestamp) and
            self.__value == other.__value and
            self.__type == other.__type and
            self.__coordinates == other.__coordinates and
            self.__ID_sensore == other.__ID_sensore and
            self.__cella == other.__cella
        )
