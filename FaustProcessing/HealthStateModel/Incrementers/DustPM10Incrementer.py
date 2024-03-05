from .Incrementer import Incrementer
from typing import List
from ..Misurazione import Misurazione
import math

class DustPM10Incrementer(Incrementer):
    def __init__(self, dust_type_naming: str = "dust_level_PM10"):
        self.__dust_type_naming = dust_type_naming
    
    def get_incrementation(self, misurazioni: List[Misurazione]):
        incremento_totale = 0
        num_misurazioni = len(misurazioni)
        for misurazione in misurazioni:
            if misurazione.get_type() == self.__dust_type_naming:
                dato = float(misurazione.get_value())
                if dato > 0:
                    incremento_totale += math.log(dato)
        return int(incremento_totale / num_misurazioni) if num_misurazioni != 0 else 0


        
