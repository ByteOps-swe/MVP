import time
import json
import random
from datetime import datetime
from typing import List
from .Simulator import Simulator
from ..Writers import Writer

class HumiditySimulator(Simulator):
    __count = 0

    def __init__(self, writer: List[Writer], latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_humidity=50):
        HumiditySimulator.__count += 1
        self.humidity = initial_humidity
        super().__init__(writer, latitude, longitude,cella,
                         f"Umd{HumiditySimulator.__count}", frequency_in_s)

    def generate_measure(self):
        # Genera una variazione casuale dell'umidità entro un intervallo realistico
        variation = random.uniform(-5, 5)  # Variazione casuale entro ±5% di umidità
        self.humidity += variation
        # Limita l'umidità tra 0% e 100% per mantenerla realistica
        self.humidity = max(0, min(100, self.humidity))

    def simulate(self) -> None:
        while super().isSimulating():
            self.generate_measure()
            data = {
                "timestamp": str(datetime.now()),
                "value": "{:.2f}".format(self.humidity),
                "type": "HumiditySimulator",
                "latitude": self.latitude,
                "longitude": self.longitude,
                "ID_sensore": self.ID_sensor,
                "cella":self.cella_sensore
            }
            super().write_to_all_writers(json.dumps(data))
            time.sleep(self.frequency)
