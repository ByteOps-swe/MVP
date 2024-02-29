import random
from .Simulator import Simulator

class ChargingStationSimulator(Simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_probability_occupied=0.5):
        ChargingStationSimulator.__count += 1
        self.__transition_probability = 0.1
        super().__init__(latitude, longitude,cella,
                         f"ChS{ChargingStationSimulator.__count}", initial_probability_occupied,"ChargingStation")

    def _generate_measure(self):
        if self._misurazione:
            new_probability = self.__transition_probability
        else:
            new_probability = 1 - self.__transition_probability
        self._misurazione = random.random() < new_probability
