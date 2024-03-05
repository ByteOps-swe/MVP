from typing import List
from .Incrementer import Incrementer
from ..Misurazione import Misurazione

class TemperatureIncrementer(Incrementer):
    """
    A class representing a temperature incrementer.

    Attributes:
        upper_health_soglia (int): The upper threshold for a healthy temperature.
        under_health_soglia (int): The lower threshold for a healthy temperature.
        temperature_type_naming (str): The naming convention for temperature type.

    Methods:
        get_incrementation(misurazioni: List[Misurazione]) -> int:
            Calculates the total incrementation based on the given measurements.

    """

    def __init__(self, upper_health_soglia: int = 20, under_health_soglia: int = 30, temperature_type_naming: str = "temperature"):
        """
        Initializes a TemperatureIncrementer object.

        Args:
            upper_health_soglia (int): The upper threshold for a healthy temperature. Default is 20.
            under_health_soglia (int): The lower threshold for a healthy temperature. Default is 30.
            temperature_type_naming (str): The naming convention for temperature type. Default is "temperature".
        """
        self.__upper_health_soglia = upper_health_soglia
        self.__under_health_soglia = under_health_soglia
        self.__temperature_type_naming = temperature_type_naming
    def get_incrementation(self, misurazioni: List[Misurazione]) -> int:
        """
        Calculates the total incrementation based on the given measurements.

        Args:
            misurazioni (List[Misurazione]): A list of measurements.

        Returns:
            int: The total incrementation.

        """
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
