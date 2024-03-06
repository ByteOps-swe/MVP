from abc import ABC, abstractmethod

class ThreadPoolTarget(ABC):
    """
    Abstract base class for a target object that can be used with a thread pool.

    Subclasses of ThreadPoolTarget must implement the `map` method.
    """

    @abstractmethod
    def map(self, func, iterable):
        """
        Apply the given function to each item in the iterable using a thread pool.

        Args:
            func: The function to apply to each item.
            iterable: The iterable containing the items to apply the function to.
        
        Returns:
            A list of results from applying the function to each item in the iterable.
        """
