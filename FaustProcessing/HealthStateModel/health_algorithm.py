from abc import ABC, abstractmethod
from typing import List
from .misurazione_salute import misurazione_salute

#Pattern Strategy
class health_algorithm(ABC):
    @abstractmethod
    def generate_new_health_score(self) -> List[misurazione_salute]:
        pass
