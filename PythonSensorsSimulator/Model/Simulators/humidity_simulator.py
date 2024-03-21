import random
from .simulator import simulator
from .sensor_types import sensor_types

class humidity_simulator(simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_humidity=50):
        humidity_simulator.__count += 1
        super().__init__(
            latitude,
            longitude,
            cella,
            f"Umd{humidity_simulator.__count}",
            initial_humidity,
            sensor_types.HUMIDITY.value
        )

    def _generate_measure(self):
        variation = random.uniform(-5, 5)
        self._misurazione += variation
        self._misurazione = max(0, min(100, self._misurazione))
