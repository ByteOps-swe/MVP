from abc import ABC, abstractmethod
from datetime import datetime
from .Misurazione import Misurazione


class Simulator(ABC): 
    def __init__(self,  latitude: float, longitude: float, cella: str, sensor_id: str, misurazione_iniziale = 0, type =""):
        self.__ID_sensor = sensor_id
        self.__cella_sensore = cella
        self.__latitude = latitude
        self.__longitude = longitude
        self._misurazione = misurazione_iniziale
        self.__type = type

    #TEMPLATEMETHOD
    def simulate(self) -> None: 
            self._generate_measure()
            while not self._filter():
             self._generate_measure() #First template step
            return Misurazione(datetime.now(), self._misurazione , self.__type,self.__latitude, self.__longitude, self.__ID_sensor,self.__cella_sensore)


    @abstractmethod
    def _generate_measure(self) -> None:
        pass
    
    #Template empty method to override
    def _filter(self) -> bool:
        return True