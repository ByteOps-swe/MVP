from abc import ABC, abstractmethod
from typing import List
from ..misurazione import misurazione

#strategy
class incrementer(ABC):

    @abstractmethod
    def get_incrementation(self, misurazioni: List[misurazione]) -> int:
        pass
