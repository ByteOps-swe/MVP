from datetime import datetime
from .Writers.Writable import Writable
from .Simulators.Misurazione import Misurazione
from .Simulators.Coordinate import Coordinate

class AdapterMisurazione(Writable):
    def __init__(self, misurazione : Misurazione):
        self.__misurazione = misurazione

    def to_json(self):
        return {
            "timestamp": str(self.__misurazione.get_timestamp()),  # Usiamo il metodo getter per ottenere il timestamp
            "value": AdapterMisurazione.__format_value(self.__misurazione.get_value()),  # Usiamo il metodo getter per ottenere il valore
            "type": self.__misurazione.get_type(),  # Usiamo il metodo getter per ottenere il tipo
            "latitude": self.__misurazione.get_latitude(),  # Usiamo il metodo getter per ottenere la latitudine
            "longitude": self.__misurazione.get_longitude(),  # Usiamo il metodo getter per ottenere la longitudine
            "ID_sensore": self.__misurazione.get_ID_sensore(),  # Usiamo il metodo getter per ottenere l'ID del sensore
            "cella": self.__misurazione.get_cella()  # Usiamo il metodo getter per ottenere il nome della cella
        }
    def get_Misurazione(self) -> Misurazione:
        return self.__misurazione
    @staticmethod
    def __format_value(value):
        if isinstance(value, bool):
            return 1 if value else 0
        if isinstance(value, float):
            return "{:.2f}".format(value)
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
        coordinate = Coordinate(latitude, longitude)
        return Misurazione(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f'), value, type_, coordinate, ID_sensore, cella)
    