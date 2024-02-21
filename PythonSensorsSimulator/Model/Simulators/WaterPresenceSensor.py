import time
import json
import random
from datetime import datetime
from typing import List
from .Simulator import Simulator
from ..Writers import Writer

class WaterPresenceSensor(Simulator):
    __count = 0

    def __init__(self, writer: List[Writer], latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, threshold=0.5):
        WaterPresenceSensor.__count += 1
        self.threshold = threshold  # soglia per rilevare la presenza di acqua
        super().__init__(writer, latitude, longitude,cella,
                         f"Wp{WaterPresenceSensor.__count}", frequency_in_s)

    def generate_measure(self):
        # Genera casualmente se la presenza di acqua supera la soglia
        water_presence = random.random() < self.threshold
        return water_presence

    def simulate(self) -> None:
        while super().isSimulating():
            water_presence = self.generate_measure()
            data = {
                "timestamp": str(datetime.now()),
                "value": int(water_presence),  # Converte True in 1 e False in 0
                "type": "WaterPresenceSensor",
                "latitude": self.latitude,
                "longitude": self.longitude,
                "ID_sensore": self.ID_sensor,
                "cella":self.cella_sensore
            }
            super().write_to_all_writers(json.dumps(data))
            time.sleep(self.frequency)
