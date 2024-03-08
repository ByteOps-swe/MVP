from typing import List
import math
from .Incrementer import Incrementer
from ..Misurazione import Misurazione

class DustPM10Incrementer(Incrementer):
    """
    A class that calculates the incrementation value based on dust PM10 measurements.

    Attributes:
        dust_type_naming (str): The name of the dust level PM10.

    Methods:
        get_incrementation: Calculates the incrementation value based on the given measurements.

    """

    def __init__(self, dust_type_naming: str = "dust_PM10"):
        self.__dust_type_naming = dust_type_naming

    def get_incrementation(self, misurazioni: List[Misurazione]):
        """
        Calculates the incrementation value based on the given measurements.

        Args:
            misurazioni (List[Misurazione]): A list of measurements.

        Returns:
            int: The calculated incrementation value.

        """
        incremento_totale = 0.0  # Change the type to float
        num_misurazioni = len(misurazioni)
        for misurazione in misurazioni:
            if misurazione.get_type() == self.__dust_type_naming:
                dato = float(misurazione.get_value())
                if dato > 0:
                    incremento_totale += math.log(dato) *  0.1
        return int(incremento_totale / num_misurazioni) if num_misurazioni != 0 else 0
