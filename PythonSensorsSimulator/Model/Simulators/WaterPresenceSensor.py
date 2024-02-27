import random
from .Simulator import Simulator
from ..Writers.Writer import Writer

class WaterPresenceSensor(Simulator):
    __count = 0

    def __init__(self, writer: Writer, latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, threshold=0.5):
        WaterPresenceSensor.__count += 1
        self.__threshold = threshold  # soglia per rilevare la presenza di acqua
        super().__init__(writer, latitude, longitude,cella,
                         f"Wp{WaterPresenceSensor.__count}", frequency_in_s,0,"WaterPresence")

    def _generate_measure(self):
        # Genera casualmente se la presenza di acqua supera la soglia
        self._misurazione = random.random() < self.__threshold
