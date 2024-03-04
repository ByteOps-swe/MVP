from abc import ABC, abstractmethod

class ThreadPoolTarget(ABC):
    @abstractmethod
    def map(self, func, iterable):
        pass