from typing import List
from .Incrementer import Incrementer
from ..Misurazione import Misurazione

class TemperatureIncrementer(Incrementer):

    def __init__(self, upper_health_soglia: int = 30, under_health_soglia: int = 20, temperature_type_naming: str = "temperature"):
        self.__upper_health_soglia = upper_health_soglia
        self.__under_health_soglia = under_health_soglia
        self.__temperature_type_naming = temperature_type_naming

    def get_incrementation(self, misurazioni: List[Misurazione]) -> int:
        incremento_totale = 0.0
        num_misurazioni = len(misurazioni)
        for misurazione in misurazioni:
            if misurazione.get_type() == self.__temperature_type_naming:
                dato = float(misurazione.get_value())
                if self.__under_health_soglia <= dato <= self.__upper_health_soglia:
                    incremento_totale += 0
                elif dato > self.__upper_health_soglia:
                    incremento_totale += dato - self.__upper_health_soglia
                else:
                    incremento_totale += self.__under_health_soglia - dato
        return int(incremento_totale / num_misurazioni) if num_misurazioni != 0 else 0
