from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Writable(ABC):
   """An abstract base class for writable objects."""

   @abstractmethod
   def to_json(self) -> str:
      """Converts the object to a JSON string representation.

      Returns:
         str: The JSON string representation of the object.
      """
      pass
