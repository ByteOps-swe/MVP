import concurrent.futures
from .thread_pool_target import thread_pool_target

class thread_pool_executor_adapter(thread_pool_target):

    def __init__(self,workers = 15):
        self.__executor = concurrent.futures.ThreadPoolExecutor(max_workers=workers)

    def map(self, func, iterable):
        return self.__executor.map(func, iterable)
