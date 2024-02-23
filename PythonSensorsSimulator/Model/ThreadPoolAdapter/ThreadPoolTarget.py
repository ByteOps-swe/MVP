from abc import ABC, abstractmethod
import concurrent.futures

class ThreadPoolTarget(ABC):
    @abstractmethod
    def map(self, func, iterable):
        pass