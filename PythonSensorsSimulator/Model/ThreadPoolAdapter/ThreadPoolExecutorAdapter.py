import concurrent.futures
from .ThreadPoolTarget import ThreadPoolTarget

class ThreadPoolExecutorAdapter(ThreadPoolTarget):
    """
    A class that adapts the ThreadPoolExecutor from the concurrent.futures module.

    This class provides a convenient way to execute functions asynchronously using a thread pool.

    Attributes:
        __executor (concurrent.futures.ThreadPoolExecutor): The underlying ThreadPoolExecutor object.

    Methods:
        map(func, iterable): Submits the given function to the thread pool for each item in the iterable.

    """

    def __init__(self):
        self.__executor = concurrent.futures.ThreadPoolExecutor()

    def map(self, func, iterable):
        """
        Submits the given function to the thread pool for each item in the iterable.

        Args:
            func (callable): The function to be executed asynchronously.
            iterable (iterable): An iterable containing the arguments to be passed to the function.

        Returns:
            concurrent.futures.Future: A future object representing the result of the function call.

        """
        return self.__executor.map(func, iterable)
