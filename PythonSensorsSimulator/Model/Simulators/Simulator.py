from abc import ABC, abstractmethod
import time
from datetime import datetime
from ..Writers.Writer import Writer
from .Misurazione import Misurazione


class Simulator(ABC):
    __writers: Writer
    __frequency: int
    __is_simulating: bool
    __ID_sensor: str
    __cella_sensore: str
    __latitude: float
    __longitude: float
    __type = str
    
    def __init__(self, writers: Writer, latitude: float, longitude: float, cella: str, sensor_id: str, frequency_in_s: int = 10, misurazione = 0, type =""):
        self.__writers = writers
        self.__frequency = frequency_in_s
        self.__is_simulating = True
        self.__ID_sensor = sensor_id
        self.__cella_sensore = cella
        self.__latitude = latitude
        self.__longitude = longitude
        self._misurazione = misurazione
        self.__type = type

    #TEMPLATEMETHOD
    def simulate(self) -> None:
        while self.__is_simulating:
            #TEMPLATING BY SUBCLASS
            self._generate_measure() #First template step
            dato = Misurazione(datetime.now(), self._misurazione , self.__type,self.__latitude, self.__longitude, self.__ID_sensor,self.__cella_sensore)
            if(self._filter()):#Second optional template step
                self.__writers.write(dato)
            time.sleep(self.__frequency)

    @abstractmethod
    def _generate_measure(self) -> None:
        pass

    def stop_simulating(self) -> None:
        self.__is_simulating = False
    
    #Template empty method to override
    def _filter(self) -> bool:
        return True