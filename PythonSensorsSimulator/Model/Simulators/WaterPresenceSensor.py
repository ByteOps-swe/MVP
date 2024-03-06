import random
from .Simulator import Simulator
from .SensorTypes import SensorTypes

class WaterPresenceSensor(Simulator):
    __count = 0

    def __init__(self, latitude: float, longitude: float, cella: str = "Centro", threshold=0.5):
        WaterPresenceSensor.__count += 1
        self.__threshold = threshold  # soglia per rilevare la presenza di acqua
        super().__init__( latitude, longitude,cella,
                         f"Wp{WaterPresenceSensor.__count}", 0,SensorTypes.WATER_PRESENCE.value)

    def _generate_measure(self):
        # Genera casualmente se la presenza di acqua supera la soglia
        self._misurazione = random.random() < self.__threshold
