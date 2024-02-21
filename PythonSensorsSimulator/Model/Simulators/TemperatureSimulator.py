import time
import json
import math
import random
from datetime import datetime
from typing import List
from .Simulator import Simulator
from ..Writers import Writer


class TemperatureSimulator(Simulator):
    __count = 0

    def __init__(self, writer: List[Writer], latitude: float, longitude: float, cella: str = "Centro", frequency_in_s: int = 5, initial_temperature=20):
        TemperatureSimulator.__count += 1
        self.temperature = initial_temperature
        # fattore di calibrazione necessario a garantire un maggiore varianza nei dati simulati dai sensori
        super().__init__(writer, latitude, longitude,cella,
                         f"Tmp{TemperatureSimulator.__count}", frequency_in_s)

    def generate_measure(self):
        # Genera una variazione casuale della temperatura entro un intervallo realistico
        variation = random.uniform(-0.5, 0.5)  # Variazione casuale entro ±0.5 gradi Celsius
        self.temperature += variation
        # Limita la temperatura tra 0 e 100 gradi Celsius per mantenerla realistica
        self.temperature = max(0, min(100, self.temperature))


    def simulate(self) -> None:
          # strettamente per il poc
        while super().isSimulating():
            self.generate_measure()
            dato = {
                "timestamp": str(datetime.now()),
                "value": "{:.2f}".format(self.temperature),
                "type": "TemperatureSimulator",
                "latitude": self.latitude,
                "longitude": self.longitude,
                "ID_sensore": self.ID_sensor,
                "cella":self.cella_sensore
            }
            super().write_to_all_writers(json.dumps(dato))
            time.sleep(self.frequency)
