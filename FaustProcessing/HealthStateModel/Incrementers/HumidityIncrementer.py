from typing import List
from .Incrementer import Incrementer
from ..Misurazione import Misurazione

class HumidityIncrementer(Incrementer):

    def __init__(self, upper_health_soglia: int = 70, under_health_soglia: int = 30, umidity_type_naming: str = "humidity"):
        self.__upper_health_soglia = upper_health_soglia
        self.__under_health_soglia = under_health_soglia
        self.__umidity_type_naming = umidity_type_naming

    def get_incrementation(self, misurazioni: List[Misurazione]):
        incremento_totale = 0.0
        num_misurazioni = len(misurazioni)
        for misurazione in misurazioni:
            # Controlla che il tipo di misurazione sia 'umidità'
            if misurazione.get_type() == self.__umidity_type_naming:
                dato = float(misurazione.get_value())
                if self.__under_health_soglia <= dato <= self.__upper_health_soglia:
                    incremento_totale += 0
                elif dato > self.__upper_health_soglia:
                    incremento_totale += dato - self.__upper_health_soglia
                else:
                    incremento_totale += self.__under_health_soglia - dato
        return int(incremento_totale / num_misurazioni) if num_misurazioni != 0 else 0
