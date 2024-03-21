import random
from .simulator import simulator
from .sensor_types import sensor_types

class electrical_fault_simulator(simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_value=0):
        electrical_fault_simulator.__count += 1
        self._fault_probability = 0.1
        super().__init__(
            latitude,
            longitude,
            cella,
            f"GstE{electrical_fault_simulator.__count}",
            initial_value,
            sensor_types.ELECTRICAL_FAULT.value
        )

    def _generate_measure(self) -> None:
        if self._misurazione == 1:
            self._fault_probability = min(0.9, self._fault_probability + 0.1)
        else:
            self._fault_probability = max(0.1, self._fault_probability - 0.1)
        self._misurazione = 1 if random.random() < self._fault_probability else 0
