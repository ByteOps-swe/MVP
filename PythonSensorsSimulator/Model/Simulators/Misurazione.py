from ..Writers.Writable import Writable

class Misurazione(Writable):
    def __init__(self, timestamp, value, type_, latitude, longitude, ID_sensore, cella):
        self.__timestamp = timestamp
        self.__value = value
        self.__type = type_
        self.__latitude = latitude
        self.__longitude = longitude
        self.__ID_sensore = ID_sensore
        self.__cella = cella

    @classmethod
    def from_json(cls, json_data):
        timestamp = json_data["timestamp"]
        value = json_data["value"]
        type_ = json_data["type"]
        latitude = json_data["latitude"]
        longitude = json_data["longitude"]
        ID_sensore = json_data["ID_sensore"]
        cella = json_data["cella"]
        return cls(timestamp, value, type_, latitude, longitude, ID_sensore, cella)

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

    @staticmethod
    def __format_value(value):
        if isinstance(value, bool):
            return 1 if value else 0
        elif isinstance(value, float):
            return "{:.2f}".format(value)
        else:
            return value
