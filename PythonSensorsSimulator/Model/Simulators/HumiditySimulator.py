import random
from .Simulator import Simulator
from ..Writers.CompositeWriter import CompositeWriter

class HumiditySimulator(Simulator):
    __count = 0

    def __init__(self, writer: CompositeWriter, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_humidity=50):
        HumiditySimulator.__count += 1
        super().__init__(writer, latitude, longitude,cella,
                         f"Umd{HumiditySimulator.__count}", frequency_in_s,initial_humidity,"HumiditySimulator")

    def _generate_measure(self):
        variation = random.uniform(-5, 5)  
        self._misurazione += variation
        self._misurazione = max(0, min(100, self._misurazione))


