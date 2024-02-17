import time
import json
import random
from datetime import datetime

from .Simulator import Simulator
from ..Writers import Writer

class EcologicalIslandSimulator(Simulator):
    __count = 0

    def __init__(self, writer: Writer, latitude: float, longitude: float,cella: str = "Centro", frequency_in_s: int = 5, initial_fill_percentage=50):
        EcologicalIslandSimulator.__count += 1
        self.fill_percentage = initial_fill_percentage
        self.max_fill_percentage = 90  # Percentuale massima di riempimento
        self.min_fill_percentage = 10  # Percentuale minima di riempimento
        self.fill_rate = 5  # Velocità di riempimento/scarico in percentuale al secondo
        super().__init__(writer, latitude, longitude,cella,
                         f"EcoIsl{EcologicalIslandSimulator.__count}", frequency_in_s)

    def generate_measure(self):
        # Aggiorna la percentuale di riempimento in base alla velocità di riempimento
        self.fill_percentage += random.uniform(-self.fill_rate, self.fill_rate)
        # Limita la percentuale di riempimento tra il valore massimo e minimo
        self.fill_percentage = max(self.min_fill_percentage, min(self.max_fill_percentage, self.fill_percentage))

    def simulate(self) -> None:
        while super().isSimulating():
            self.generate_measure()
            data = {
                "timestamp": str(datetime.now()),
                "value": "{:.2f}".format(self.fill_percentage),
                "type": "EcologicalIslandSimulator",
                "latitude": self.latitude,
                "longitude": self.longitude,
                "ID_sensore": self.ID_sensor,
                "cella":self.cella_sensore
            }
            self.writer.write(json.dumps(data))
            time.sleep(self.frequency)
