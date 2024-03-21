import random
from .simulator import simulator
from .sensor_types import sensor_types

class charging_station_simulator(simulator):
    __count = 0
    __transition_probability = 0.1
    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_value=0):
        charging_station_simulator.__count += 1
        charging_station_simulator.__transition_probability = 0.1
        super().__init__(
            latitude,
            longitude,
            cella,
            f"ChS{charging_station_simulator.__count}",
            initial_value,
            sensor_types.CHARGING_STATION.value
        )

    def _generate_measure(self):
        if self._misurazione:
            new_probability = charging_station_simulator.__transition_probability
        else:
            new_probability = 1 - charging_station_simulator.__transition_probability
        self._misurazione = random.random() < new_probability
