from abc import ABC, abstractmethod


class Writer(ABC):

    @abstractmethod
    def write(self, to_write: str) -> None:
        pass
