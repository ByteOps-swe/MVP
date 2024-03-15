from abc import ABC, abstractmethod

class thread_pool_target(ABC):

    @abstractmethod
    def map(self, func, iterable):
        pass
