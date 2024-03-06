import random
from .Simulator import Simulator
from .SensorTypes import SensorTypes

class TemperatureSimulator(Simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_temperature=20):
        TemperatureSimulator.__count += 1
        super().__init__( latitude, longitude,cella,
                         f"Tmp{TemperatureSimulator.__count}", initial_temperature,SensorTypes.TEMPERATURE.value)

    def _generate_measure(self) -> None:
        variation = random.uniform(-0.5, 0.5)  
        self._misurazione += variation
        self._misurazione = max(0, min(100, self._misurazione))