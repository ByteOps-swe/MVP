from abc import ABC, abstractmethod
from datetime import datetime
from .misurazione import misurazione
from .coordinate import coordinate

class simulator(ABC):
    def __init__(self,  latitude: float, longitude: float, cella: str, sensor_id: str, misurazione_iniziale = 0, _type =""):
        self.__ID_sensor = sensor_id
        self.__cella_sensore = cella
        self.__coordinate = coordinate(latitude,longitude)
        self._misurazione = misurazione_iniziale
        self.__type = _type

    #TEMPLATEMETHOD
    def simulate(self) -> misurazione:
        self._generate_measure()
        self._adapt()
        return misurazione(
            datetime.now(),
            self._misurazione,
            self.__type,
            self.__coordinate,
            self.__ID_sensor,
            self.__cella_sensore
        )

    @abstractmethod
    def _generate_measure(self) -> None:
        pass

    def _adapt(self) -> None:
        pass
