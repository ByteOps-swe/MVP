import random
from .simulator import simulator
from .sensor_types import sensor_types

class water_presence_sensor(simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", threshold=0.5):
        water_presence_sensor.__count += 1
        self.__threshold = threshold
        super().__init__(
            latitude,
            longitude,
            cella,
            f"Wp{water_presence_sensor.__count}",
            0,
            sensor_types.WATER_PRESENCE.value)

    def _generate_measure(self):
        self._misurazione = random.random() < self.__threshold
