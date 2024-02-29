import random
from .Simulator import Simulator


class ElectricalFaultSimulator(Simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_value=0):
        ElectricalFaultSimulator.__count += 1
        self._fault_probability = 0.1
        super().__init__(latitude, longitude, cella,
                         f"GstE{ElectricalFaultSimulator.__count}",initial_value, "guastoElettrico")

    def _generate_measure(self) -> None:
        if self._misurazione == 1:
            self._fault_probability = min(0.9, self._fault_probability + 0.1)
        else:
            self._fault_probability = max(0.1, self._fault_probability - 0.1)
        self._misurazione = 1 if random.random() < self._fault_probability else 0
