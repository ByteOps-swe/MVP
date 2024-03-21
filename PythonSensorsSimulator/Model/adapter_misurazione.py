from datetime import datetime
from .Writers.writable import writable
from .Simulators.misurazione import misurazione
from .Simulators.coordinate import coordinate

class adapter_misurazione(writable):
    def __init__(self, measure : misurazione):
        self.__misurazione = measure

    def to_json(self):
        return {
            "timestamp": str(self.__misurazione.get_timestamp()),
            "value": adapter_misurazione.__format_value(self.__misurazione.get_value()),
            "type": self.__misurazione.get_type(),
            "latitude": self.__misurazione.get_latitude(),
            "longitude": self.__misurazione.get_longitude(),
            "ID_sensore": self.__misurazione.get_ID_sensore(),
            "cella": self.__misurazione.get_cella()
        }
    def get_misurazione(self) -> misurazione:
        return self.__misurazione

    @staticmethod
    def __format_value(value):
        if isinstance(value, bool):
            return 1 if value else 0
        return value

    @staticmethod
    def from_json(json_data:dict):
        timestamp = json_data["timestamp"]
        value = json_data["value"]
        type_ = json_data["type"]
        latitude = json_data["latitude"]
        longitude = json_data["longitude"]
        ID_sensore = json_data["ID_sensore"]
        cella = json_data["cella"]
        coord = coordinate(latitude, longitude)
        return misurazione(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f'), value, type_, coord, ID_sensore, cella)
