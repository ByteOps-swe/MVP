from .Writers.Writable import Writable
class Misurazione(Writable):
    def __init__(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        self.__timestamp = timestamp
        self.__value = value
        self.__type = type_
        self.__latitude = latitude
        self.__longitude = longitude
        self.__ID_sensore = ID_sensore
        self.__cella = cella

    def to_json(self):
        return {
            "timestamp": str(self.__timestamp),
            "value": Misurazione.__format_value(self.__value),
            "type": self.__type,
            "latitude": self.__latitude,
            "longitude": self.__longitude,
            "ID_sensore": self.__ID_sensore,
            "cella": self.__cella
        }

    def get_timestamp(self):
        return self.__timestamp

    def get_value(self):
        return self.__value

    def get_type(self):
        return self.__type

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude

    def get_ID_sensore(self):
        return self.__ID_sensore

    def get_cella(self):
        return self.__cella
