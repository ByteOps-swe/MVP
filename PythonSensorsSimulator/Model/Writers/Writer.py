from abc import ABC, abstractmethod
from .Writable import Writable
#Pattern Strategy
from abc import ABC, abstractmethod
from typing import Any

class Writer(ABC):
    """
    Abstract base class for writers.

    This class defines the interface for writing data to a specific destination.
    Subclasses must implement the `write` method.

    Attributes:
        None

    Methods:
        write: Writes the given data to the destination.

    """

    @abstractmethod
    def write(self, to_write: Any) -> None:
        """
        Writes the given data to the destination.

        Args:
            to_write: The data to be written.

        Returns:
            None

        """
        pass
class Writer(ABC):

    @abstractmethod
    def write(self, to_write: Writable) -> None:
        pass
