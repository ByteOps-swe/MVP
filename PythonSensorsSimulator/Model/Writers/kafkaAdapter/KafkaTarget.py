from abc import ABC, abstractmethod
#CLASSE TARGET
class KafkaTarget(ABC):
    @abstractmethod
    def write_to_kafka(self, topic: str, data: str) -> None:
        pass
    @abstractmethod
    def flush_kafka_producer(self):
        pass