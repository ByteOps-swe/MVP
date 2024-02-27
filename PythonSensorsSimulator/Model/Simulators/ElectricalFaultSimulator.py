import random
from .Simulator import Simulator
from ..Writers.Writer import Writer


class ElectricalFaultSimulator(Simulator):
    __count = 0

    def __init__(self, writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_fault_probability=0.1):
        ElectricalFaultSimulator.__count += 1
        super().__init__(writer, latitude, longitude, cella,
                         f"GstE{ElectricalFaultSimulator.__count}", frequency_in_s, "guastoElettrico")
        self._fault_probability = initial_fault_probability

    def _generate_measure(self) -> None:
        if self._misurazione == 1:
            self._fault_probability = min(0.9, self._fault_probability + 0.1)
        else:
            self._fault_probability = max(0.1, self._fault_probability - 0.1)
        self._misurazione = 1 if random.random() < self._fault_probability else 0
