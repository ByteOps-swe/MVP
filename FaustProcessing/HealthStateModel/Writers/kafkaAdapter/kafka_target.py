from abc import ABC, abstractmethod

class kafka_target(ABC):

    @abstractmethod
    def write_to_kafka(self, data) -> None:
        pass

    @abstractmethod
    def flush_kafka_producer(self):
        pass
