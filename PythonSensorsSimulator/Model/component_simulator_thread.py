import threading
from abc import  abstractmethod

class component_simulator_thread(threading.Thread):

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def task(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass
