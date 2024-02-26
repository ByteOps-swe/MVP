from abc import ABC, abstractmethod


# Pattern Strategy per il calcolo
class Incrementer(ABC):

    @abstractmethod
    def get_incrementation(self, misurazioni) -> int:
        pass
