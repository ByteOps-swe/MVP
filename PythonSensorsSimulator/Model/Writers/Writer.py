from abc import ABC, abstractmethod

#Strategy
class Writer(ABC):

    @abstractmethod
    def write(self, to_write: str) -> None:
        pass
