import random
from .Simulator import Simulator
from ..Writers.Writer import Writer


class DustPM10Simulator(Simulator):
    __count = 0

    def __init__(self, writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_dust_level=30):
        DustPM10Simulator.__count += 1
        super().__init__(writer, latitude, longitude,cella,
                         f"DstPM10{DustPM10Simulator.__count}", frequency_in_s,initial_dust_level,"dust_level_PM10")

    def _generate_measure(self) -> None:
        variation = random.uniform(-5, 5)  # Variability in measurements
        self._misurazione += variation
        self._misurazione = max(0, min(100, self._misurazione))  # Ensuring measurements stay within a valid range


