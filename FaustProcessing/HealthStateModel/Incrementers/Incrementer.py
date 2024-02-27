from abc import ABC, abstractmethod
from typing import List
from Misurazione import Misurazione

#strategy
class Incrementer(ABC):

    @abstractmethod
    def get_incrementation(self, misurazioni: List[Misurazione]) -> int:
        pass
