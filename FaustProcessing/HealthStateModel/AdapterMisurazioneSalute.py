from .Writers.Writable import Writable
from .MisurazioneSalute import MisurazioneSalute
class AdapterMisurazione(Writable):
    def __init__(self, misurazione : MisurazioneSalute):
        self.__misurazione = misurazione

    def to_json(self):
        return {
            "timestamp": str(self.__misurazione.get_timestamp()),
            "value":self.__misurazione.get_value(),
            "type": self.__misurazione.get_type(),
            "cella": self.__misurazione.get_cella()
        }
