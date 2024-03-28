import random
from .simulator import simulator
from .sensor_types import sensor_types

class temperature_simulator(simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_temperature=20):
        temperature_simulator.__count += 1
        super().__init__(
            latitude,
            longitude,
            cella,
            f"Tmp{temperature_simulator.__count}",
            initial_temperature,
            sensor_types.TEMPERATURE.value
        )

    def _generate_measure(self) -> None:
        variation = random.uniform(-0.5, 0.5)
        new_measurement = self._misurazione + variation
        if -15 <= new_measurement <= 45:
            self._misurazione = new_measurement
        if self._misurazione < -15:
            self._misurazione += 0.5
        if self._misurazione > 45:
            self._misurazione -= 0.5
