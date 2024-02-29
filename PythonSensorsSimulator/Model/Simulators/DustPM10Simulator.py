import random
from .Simulator import Simulator


class DustPM10Simulator(Simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", initial_dust_level=30):
        DustPM10Simulator.__count += 1
        super().__init__( latitude, longitude,cella,
                         f"DstPM10{DustPM10Simulator.__count}", initial_dust_level,"dust_level_PM10")

    def _generate_measure(self) -> None:
        variation = random.uniform(-5, 5)  
        self._misurazione += variation
        self._misurazione = max(0, min(100, self._misurazione)) 


