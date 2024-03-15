from abc import ABC, abstractmethod

class kafka_target(ABC):
    """
    Abstract base class for writing data to Kafka.
    """

    @abstractmethod
    def write_to_kafka(self, data: str) -> None:
        """
        Writes the given data to Kafka.

        Args:
            data (str): The data to be written to Kafka.

        Returns:
            None
        """
            