import random
from .Simulator import Simulator

class EcologicalIslandSimulator(Simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float,cella: str = "Centro", initial_fill_percentage=50):
        EcologicalIslandSimulator.__count += 1
        self.__max_fill_percentage = 90  
        self.__min_fill_percentage = 10  
        self.__fill_rate = 5  
        super().__init__(latitude, longitude,cella,
                         f"EcoIsl{EcologicalIslandSimulator.__count}", initial_fill_percentage,"EcologicalIsland")

    def _generate_measure(self):
        self._misurazione += random.uniform(-self.__fill_rate, self.__fill_rate)
        self._misurazione = max(self.__min_fill_percentage, min(self.__max_fill_percentage, self._misurazione))
