import random
from .simulator import simulator
from .sensor_types import sensor_types

class temperature_simulator(simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_temperature=20):
        temperature_simulator.__count += 1
        super().__init__( latitude, longitude,cella,
                         f"Tmp{temperature_simulator.__count}", initial_temperature,sensor_types.TEMPERATURE.value)

    def _generate_measure(self) -> None:
        variation = random.uniform(-0.5, 0.5)
        self._misurazione += variation
        self._misurazione = max(0, min(100, self._misurazione))
