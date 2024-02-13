from .Writer import Writer


class StdoutWriter(Writer):
    def write(self, to_write: str) -> None:
        print(to_write + '\n')
