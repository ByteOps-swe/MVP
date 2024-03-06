import random
from .Simulator import Simulator
from .SensorTypes import SensorTypes

class ChargingStationSimulator(Simulator):
    __count = 0
    __transition_probability = 0.1
    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_value=0):
        ChargingStationSimulator.__count += 1
        ChargingStationSimulator.__transition_probability = 0.1
        super().__init__(latitude, longitude,cella,
                         f"ChS{ChargingStationSimulator.__count}", initial_value, SensorTypes.CHARGING_STATION.value)

    def _generate_measure(self):
        if self._misurazione:
            new_probability = ChargingStationSimulator.__transition_probability
        else:
            new_probability = 1 - ChargingStationSimulator.__transition_probability
        self._misurazione = random.random() < new_probability
