from typing import List
import math
from .incrementer import incrementer
from ..misurazione import misurazione
from ..sensor_types import sensor_types
class dust_PM10_incrementer(incrementer):
    def __init__(self, dust_type_naming: str = sensor_types.DUST_PM10.value):
        self.__dust_type_naming = dust_type_naming

    def get_incrementation(self, misurazioni: List[misurazione]):
        incremento_totale = 0.0  # Change the type to float
        num_misurazioni = len(misurazioni)
        for misurazione in misurazioni:
            if misurazione.get_type() == self.__dust_type_naming:
                dato = float(misurazione.get_value())
                if dato > 0:
                    incremento_totale += math.log(dato) *  0.1
        return int(incremento_totale / num_misurazioni) if num_misurazioni != 0 else 0
