import concurrent.futures
from .ThreadPoolTarget import ThreadPoolTarget

class ThreadPoolExecutorAdapter(ThreadPoolTarget):
    def __init__(self):
        self.__executor = concurrent.futures.ThreadPoolExecutor()

    def map(self, func, iterable):
        return self.__executor.map(func, iterable)