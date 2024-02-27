from .Incrementer import Incrementer
from typing import List
from Misurazione import Misurazione

class TemperatureIncrementer(Incrementer):
    def __init__(self, upper_health_soglia=20, under_health_soglia=30):
        self.__upper_health_soglia = upper_health_soglia
        self.__under_health_soglia = under_health_soglia
    
    def get_incrementation(self, misurazioni: List[Misurazione]):
        incremento_totale = 0
        num_misurazioni = len(misurazioni)
        for misurazione in misurazioni:
            dato = float(misurazione.get_value())
            if self.__under_health_soglia <= dato <= self.__upper_health_soglia:
                incremento_totale += 0
            elif dato > self.__upper_health_soglia:
                incremento_totale += dato - self.__upper_health_soglia
            else:
                incremento_totale += self.__under_health_soglia - dato
        return int(incremento_totale / num_misurazioni) if num_misurazioni != 0 else 0


        
