from abc import ABC, abstractmethod
from .Writable import Writable
#Pattern Strategy
@abstractmethod
class Writer(ABC):

    @abstractmethod
    def write(self, to_write: Writable) -> None:
        pass
