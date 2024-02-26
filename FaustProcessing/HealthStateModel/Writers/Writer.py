from abc import ABC, abstractmethod
from ..MisurazioneSalute import MisurazioneSalute

#Pattern Strategy
class Writer(ABC):

    @abstractmethod
    def write(self, to_write: MisurazioneSalute) -> None:
        pass
