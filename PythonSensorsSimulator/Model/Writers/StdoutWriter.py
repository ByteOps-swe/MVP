from .Writer import Writer
from ..Simulators.Misurazione import Misurazione


class StdoutWriter(Writer):
    def write(self, to_write: Misurazione) -> None:
        print(to_write.to_json() + '\n')
