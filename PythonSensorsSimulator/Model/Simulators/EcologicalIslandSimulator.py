import random
from .Simulator import Simulator
from .SensorTypes import SensorTypes
class EcologicalIslandSimulator(Simulator):
    __count = 0
    __max_fill_percentage = 90  
    __min_fill_percentage = 10  
    __fill_rate = 5  

    def __init__(self, latitude: float, longitude: float,cella: str = "Centro", initial_fill_percentage=50):
        EcologicalIslandSimulator.__count += 1
       
        super().__init__(latitude, longitude,cella,
                         f"EcoIsl{EcologicalIslandSimulator.__count}", initial_fill_percentage,SensorTypes.ECOLOGICAL_ISLAND.value)

    def _generate_measure(self):
        self._misurazione += random.uniform(-EcologicalIslandSimulator.__fill_rate, EcologicalIslandSimulator.__fill_rate)
        self._misurazione = max(EcologicalIslandSimulator.__min_fill_percentage, min(EcologicalIslandSimulator.__max_fill_percentage, self._misurazione))
