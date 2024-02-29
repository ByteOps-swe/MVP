from .Writers.Writable import Writable
from .Simulators.Misurazione import Misurazione
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

    @staticmethod
    def __format_value(value):
        if isinstance(value, bool):
            return 1 if value else 0
        elif isinstance(value, float):
            return "{:.2f}".format(value)
        else:
            return value