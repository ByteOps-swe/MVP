from abc import ABC, abstractmethod
from .MisurazioneSalute import MisurazioneSalute
from typing import List

#Pattern Strategy
class HealthAlgorithm(ABC):
    @abstractmethod
    def generate_new_health_score(self) -> List[MisurazioneSalute]:
        pass
