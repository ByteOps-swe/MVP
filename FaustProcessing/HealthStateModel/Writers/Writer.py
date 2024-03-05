from abc import ABC, abstractmethod
from .Writable import Writable
#Pattern Strategy
class Writer(ABC):
    """
    Abstract base class for writers.
    """
    @abstractmethod
    def write(self, to_write: Writable) -> None:
        """
        Abstract method to write data.

        Args:
            to_write: The data to be written.
        """
