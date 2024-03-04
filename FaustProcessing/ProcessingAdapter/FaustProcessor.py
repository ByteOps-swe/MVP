from abc import ABC, abstractmethod
from .FaustMeasurement import FaustMeasurement
#strategy
class Processor(ABC):
    @abstractmethod
    def process(self,misurazione:FaustMeasurement) -> None:
        pass
