import time
import json
import random
from datetime import datetime

from .Simulator import Simulator
from ..Writers import Writer

class HumiditySimulator(Simulator):
    __count = 0

    def __init__(self, writer: Writer, latitude: float, longitude: float, frequency_in_s: int = 5, initial_humidity=50):
        HumiditySimulator.__count += 1
        self.humidity = initial_humidity
        super().__init__(writer, latitude, longitude,
                         f"Umd{HumiditySimulator.__count}", frequency_in_s)

    def generate_measure(self):
        # Genera una variazione casuale dell'umidità entro un intervallo realistico
        variation = random.uniform(-5, 5)  # Variazione casuale entro ±5% di umidità
        self.humidity += variation
        # Limita l'umidità tra 0% e 100% per mantenerla realistica
        self.humidity = max(0, min(100, self.humidity))

    def simulate(self) -> None:
        while super().continue_simulating():
            self.generate_measure()
            data = {
                "timestamp": str(datetime.now()),
                "value": "{:.2f}".format(self.humidity),
                "type": "HumiditySimulator",
                "latitude": self._latitude,
                "longitude": self._longitude,
                "ID_sensore": self._sensor_name
            }
            self._writer.write(json.dumps(data))
            time.sleep(self._frequency_in_s)
