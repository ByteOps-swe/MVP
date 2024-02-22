import random
from typing import List
from .Simulator import Simulator
from ..Writers import Writer

class ChargingStationSimulator(Simulator):
    __count = 0

    def __init__(self, writer: List[Writer], latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_probability_occupied=0.5):
        ChargingStationSimulator.__count += 1
        self.__transition_probability = 0.1
        super().__init__(writer, latitude, longitude,cella,
                         f"ChS{ChargingStationSimulator.__count}", frequency_in_s,initial_probability_occupied,"ChargingStationSimulator")

    def _generate_measure(self):
        if self._misurazione:
            new_probability = self.__transition_probability
        else:
            new_probability = 1 - self.__transition_probability
        self._misurazione = random.random() < new_probability
