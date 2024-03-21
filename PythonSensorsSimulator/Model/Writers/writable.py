from abc import ABC, abstractmethod

class writable(ABC):
    @abstractmethod
    def to_json(self) -> str:
        pass
