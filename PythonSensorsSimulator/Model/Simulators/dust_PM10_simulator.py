import random
from .simulator import simulator
from .sensor_types import sensor_types

class dust_PM10_simulator(simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_dust_level=30):
        dust_PM10_simulator.__count += 1
        super().__init__( latitude, longitude,cella,
                         f"DstPM10{dust_PM10_simulator.__count}", initial_dust_level,sensor_types.DUST_PM10.value)

    def _generate_measure(self) -> None:
        variation = random.uniform(-5, 5)
        self._misurazione += variation
        self._misurazione = max(0, min(100, self._misurazione))
