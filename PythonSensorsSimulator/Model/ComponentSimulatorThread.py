import threading
from abc import  abstractmethod

class ComponentSimulatorThread(threading.Thread):

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass
