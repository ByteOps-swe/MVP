import time
import json
import random
from datetime import datetime

from .Simulator import Simulator
from ..Writers import Writer

class ChargingStationSimulator(Simulator):
    __count = 0

    def __init__(self, writer: Writer, latitude: float, longitude: float, frequency_in_s: int = 5, initial_probability_occupied=0.5):
        ChargingStationSimulator.__count += 1
        self.occupied = random.random() < initial_probability_occupied
        self.transition_probability = 0.1
        super().__init__(writer, latitude, longitude,
                         f"Colonnina di Ricarica {ChargingStationSimulator.__count}", frequency_in_s)

    def generate_measure(self):
        if self.occupied:
            new_probability = self.transition_probability
        else:
            new_probability = 1 - self.transition_probability
        self.occupied = random.random() < new_probability

    def simulate(self) -> None:
        while super().continue_simulating():
            self.generate_measure()
            data = {
                "timestamp": str(datetime.now()),
                "value": int(self.occupied),
                "type": "ChargingStationSimulator",
                "latitude": self._latitude,
                "longitude": self._longitude,
                "sensor_name": self._sensor_name
            }
            self._writer.write(json.dumps(data))
            time.sleep(self._frequency_in_s)
