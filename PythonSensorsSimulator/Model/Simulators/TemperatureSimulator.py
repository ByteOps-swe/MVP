import random
from .Simulator import Simulator
from ..Writers.Writer import Writer


class TemperatureSimulator(Simulator):
    __count = 0

    def __init__(self, writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_temperature=20):
        TemperatureSimulator.__count += 1
        super().__init__(writer, latitude, longitude,cella,
                         f"Tmp{TemperatureSimulator.__count}", frequency_in_s,initial_temperature,"TemperatureSimulator")

    def _generate_measure(self) -> None:
        variation = random.uniform(-0.5, 0.5)  
        self._misurazione += variation
        self._misurazione = max(0, min(100, self._misurazione))