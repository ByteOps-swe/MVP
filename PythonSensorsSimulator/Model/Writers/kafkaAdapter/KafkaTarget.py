from abc import ABC, abstractmethod
#CLASSE TARGET
class KafkaTarget(ABC):
    """
    Abstract base class for Kafka targets.
    """

    @abstractmethod
    def write_to_kafka(self, data: str) -> None:
        """
        Writes data to Kafka.

        Args:
            data (str): The data to be written to Kafka.
        """
    @abstractmethod
    def flush_kafka_producer(self):
        """
        Flushes the Kafka producer.
        """
