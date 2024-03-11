from abc import ABC, abstractmethod
from typing import List
from .MisurazioneSalute import MisurazioneSalute

#Pattern Strategy
class HealthAlgorithm(ABC):
    @abstractmethod
    def generate_new_health_score(self) -> List[MisurazioneSalute]:
        pass
