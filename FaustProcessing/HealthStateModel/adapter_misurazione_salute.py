from .Writers.writable import writable
from .misurazione_salute import misurazione_salute

class adapter_misurazione(writable):
    def __init__(self, misurazione : misurazione_salute):
        self.__misurazione = misurazione

    def to_json(self):
        return {
            "timestamp": str(self.__misurazione.get_timestamp()),
            "value":self.__misurazione.get_value(),
            "type": self.__misurazione.get_type(),
            "cella": self.__misurazione.get_cella()
        }
