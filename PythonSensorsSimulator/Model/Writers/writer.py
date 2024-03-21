from abc import ABC, abstractmethod
from .writable import writable
#Pattern Strategy
@abstractmethod
class writer(ABC):

    @abstractmethod
    def write(self, to_write: writable) -> None:
        pass
