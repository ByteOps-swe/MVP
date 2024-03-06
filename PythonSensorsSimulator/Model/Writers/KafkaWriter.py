import json
from threading import Lock
from .Writer import Writer
from .kafkaAdapter.KafkaTarget import KafkaTarget
from .Writable import Writable

class KafkaWriter(Writer):
    """
    A class that writes data to a Kafka target.

    Attributes:
        __lock (Lock): A lock to ensure thread-safe access to the KafkaTarget.
        __kafka_target (KafkaTarget): The Kafka target to write data to.
    """

    __lock: Lock = Lock()

    def __init__(self, kafka_target: KafkaTarget):
        """
        Initializes a KafkaWriter instance.

        Args:
            kafka_target (KafkaTarget): The Kafka target to write data to.
        """
        self.__kafka_target = kafka_target

    def write(self, to_write: Writable) -> None:
        """
        Writes the given data to the Kafka target.

        Args:
            to_write (Writable): The data to write.

        Returns:
            None
        """
        with self.__lock:
            self.__kafka_target.write_to_kafka(json.dumps(to_write.to_json()))

    def flush_kafka_producer(self):
        """
        Flushes the Kafka producer.

        Returns:
            None
        """
        self.__kafka_target.flush_kafka_producer()
