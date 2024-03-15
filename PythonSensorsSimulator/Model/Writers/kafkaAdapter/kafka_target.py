from abc import ABC, abstractmethod
#CLASSE TARGET
class kafka_target(ABC):

    @abstractmethod
    def write_to_kafka(self, data: str) -> None:
        pass

    @abstractmethod
    def flush_kafka_producer(self):
        pass
