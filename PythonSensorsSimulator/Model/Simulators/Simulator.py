from abc import ABC, abstractmethod
from datetime import datetime
from .Misurazione import Misurazione
from .Coordinate import Coordinate
import random
from datetime import timedelta
class Simulator(ABC): 
    __start_date = datetime(2024, 1, 1)  
    __end_date = datetime(2024, 12, 31)  

    def __init__(self,  latitude: float, longitude: float, cella: str, sensor_id: str, misurazione_iniziale = 0, type =""):
        self.__ID_sensor = sensor_id
        self.__cella_sensore = cella
        self.__coordinate = Coordinate(latitude,longitude)
        self._misurazione = misurazione_iniziale
        self.__type = type

    #TEMPLATE METHOD
    def simulate(self) -> None: 
        self._generate_measure()
        while not self._filter():
            self._generate_measure()  # First template step
        return Misurazione(self._random_datetime(), self._misurazione, self.__type, self.__coordinate, self.__ID_sensor, self.__cella_sensore)

    @abstractmethod
    def _generate_measure(self) -> None:
        pass

    # Template empty method to override
    def _filter(self) -> bool:
        return True

    def _random_datetime(self) -> datetime:
        delta = Simulator.__end_date - Simulator.__start_date
        random_seconds = random.randint(0, delta.total_seconds())
        random_timedelta = timedelta(seconds=random_seconds)
        return Simulator.__start_date + random_timedelta