from abc import ABC, abstractmethod
from datetime import datetime
from .Misurazione import Misurazione
from .Coordinate import Coordinate

class Simulator(ABC):
    def __init__(self,  latitude: float, longitude: float, cella: str, sensor_id: str, misurazione_iniziale = 0, _type =""):
        self.__ID_sensor = sensor_id
        self.__cella_sensore = cella
        self.__coordinate = Coordinate(latitude,longitude)
        self._misurazione = misurazione_iniziale
        self.__type = _type

    #TEMPLATEMETHOD
    def simulate(self) -> Misurazione:
        self._generate_measure()
        while not self._filter():
            self._generate_measure() #First template step
        return Misurazione(datetime.now(), self._misurazione , self.__type, self.__coordinate, self.__ID_sensor,self.__cella_sensore)

    @abstractmethod
    def _generate_measure(self) -> None:
        pass

    #Template empty method to override
    def _filter(self) -> bool:
        return True
