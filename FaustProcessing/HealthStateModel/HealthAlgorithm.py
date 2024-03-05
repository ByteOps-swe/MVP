from abc import ABC, abstractmethod
from .MisurazioneSalute import MisurazioneSalute
#Pattern Strategy
class HealthAlgorithm(ABC):
    """
    Abstract base class for health algorithms.

    This class defines the interface for generating a new health score.

    Attributes:
        None

    Methods:
        generate_new_health_score: Abstract method that generates a new health score.

    """

    @abstractmethod
    def generate_new_health_score(self) -> MisurazioneSalute:
        """
        Abstract method that generates a new health score.

        Returns:
            MisurazioneSalute: The newly generated health score.

        """
        pass