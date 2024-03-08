from abc import ABC, abstractmethod
from .MisurazioneSalute import MisurazioneSalute
#Pattern Strategy
class HealthAlgorithm(ABC):
    @abstractmethod
    def generate_new_health_score(self) -> MisurazioneSalute:
        pass
