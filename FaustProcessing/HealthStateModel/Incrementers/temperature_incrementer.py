from typing import List
from .incrementer import incrementer
from .health_constant import health_constant
from ..misurazione import misurazione
from ..sensor_types import sensor_types

class temperature_incrementer(incrementer):

    def __init__(self, upper_health_soglia: int = health_constant.TEMPERATURE_UPPER_HEALTH.value, under_health_soglia: int = health_constant.TEMPERATURE_UNDER_HEALTH.value, temperature_type_naming: str = sensor_types.TEMPERATURE.value):
        self.__upper_health_soglia = upper_health_soglia
        self.__under_health_soglia = under_health_soglia
        self.__temperature_type_naming = temperature_type_naming

    def get_incrementation(self, misurazioni: List[misurazione]) -> int:
        incremento_totale = 0.0
        num_misurazioni = len(misurazioni)
        for misurazione in misurazioni:
            if misurazione.get_type() == self.__temperature_type_naming:
                dato = float(misurazione.get_value())
                if dato > self.__upper_health_soglia:
                    incremento_totale += dato - self.__upper_health_soglia
                elif dato < self.__under_health_soglia:
                    incremento_totale += self.__under_health_soglia - dato
        return int(incremento_totale / num_misurazioni) if num_misurazioni != 0 else 0
