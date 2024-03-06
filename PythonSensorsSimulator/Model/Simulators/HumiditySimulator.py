import random
from .Simulator import Simulator
from .SensorTypes import SensorTypes

class HumiditySimulator(Simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_humidity=50):
        HumiditySimulator.__count += 1
        super().__init__(latitude, longitude,cella,
                         f"Umd{HumiditySimulator.__count}",initial_humidity,SensorTypes.HUMIDITY.value)

    def _generate_measure(self):
        variation = random.uniform(-5, 5)
        self._misurazione += variation
        self._misurazione = max(0, min(100, self._misurazione))
