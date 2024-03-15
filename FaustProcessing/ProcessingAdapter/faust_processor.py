from abc import ABC, abstractmethod
from .faust_measurement import faust_measurement
#strategy
class processor(ABC):
    @abstractmethod
    async def process(self,misurazione:faust_measurement):
        pass
