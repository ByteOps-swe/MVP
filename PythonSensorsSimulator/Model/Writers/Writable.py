from abc import ABC, abstractmethod
class Writable(ABC):
     @abstractmethod
     def to_json(self) -> str:
        pass