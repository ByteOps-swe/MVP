from abc import ABC, abstractmethod
from .writable import writable
#Pattern Strategy
class writer(ABC):
    """
    Abstract base class for writers.
    """
    @abstractmethod
    def write(self, to_write: writable) -> None:
        """
        Abstract method to write data.

        Args:
            to_write: The data to be written.
        """
