import random
from .simulator import simulator
from .sensor_types import sensor_types
class ecological_island_simulator(simulator):
    __count = 0
    __max_fill_percentage = 90
    __min_fill_percentage = 10
    __fill_rate = 5

    def __init__(self, latitude: float, longitude: float,cella: str = "Centro", initial_fill_percentage=50):
        ecological_island_simulator.__count += 1
        super().__init__(latitude, longitude,cella,
                         f"EcoIsl{ecological_island_simulator.__count}", initial_fill_percentage,sensor_types.ECOLOGICAL_ISLAND.value)

    def _generate_measure(self):
        self._misurazione += random.uniform(-ecological_island_simulator.__fill_rate, ecological_island_simulator.__fill_rate)
        self._misurazione = max(ecological_island_simulator.__min_fill_percentage,
                              min(ecological_island_simulator.__max_fill_percentage, self._misurazione))
