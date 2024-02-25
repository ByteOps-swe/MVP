import random
from .Simulator import Simulator
from ..Writers.Writer import Writer

class EcologicalIslandSimulator(Simulator):
    __count = 0

    def __init__(self, writer: Writer, latitude: float, longitude: float,cella: str = "Centro", frequency_in_s: int = 5, initial_fill_percentage=50):
        EcologicalIslandSimulator.__count += 1
        self.__max_fill_percentage = 90  
        self.__min_fill_percentage = 10  
        self.__fill_rate = 5  
        super().__init__(writer, latitude, longitude,cella,
                         f"EcoIsl{EcologicalIslandSimulator.__count}", frequency_in_s,initial_fill_percentage,"EcologicalIslandSimulator")

    def _generate_measure(self):
        self._misurazione += random.uniform(-self.__fill_rate, self.__fill_rate)
        self._misurazione = max(self.__min_fill_percentage, min(self.__max_fill_percentage, self._misurazione))
