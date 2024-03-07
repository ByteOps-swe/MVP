import concurrent.futures
from .ThreadPoolTarget import ThreadPoolTarget

class ThreadPoolExecutorAdapter(ThreadPoolTarget):

    def __init__(self,workers = 15):
        self.__executor = concurrent.futures.ThreadPoolExecutor(max_workers=workers)

    def map(self, func, iterable):
        return self.__executor.map(func, iterable)
