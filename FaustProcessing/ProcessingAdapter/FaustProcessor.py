from abc import ABC, abstractmethod
from .FaustMeasurement import FaustMeasurement
#strategy
class Processor(ABC):
    @abstractmethod
    async def process(self,misurazione:FaustMeasurement):
        pass
