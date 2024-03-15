import json
import threading
from .writer import writer
from .KafkaAdapter.kafka_target import kafka_target
from .writable import writable

class kafka_writer(writer):
    """
    A class that writes data to a Kafka target.

    Attributes:
        __lock (Lock): A lock to ensure thread-safe access to the kafka_target.
        __kafka_target (kafka_target): The Kafka target to write to.
    """

    def __init__(self, kafka_targ: kafka_target):
        """
        Initializes a kafka_writer instance.

        Args:
            kafka_target (kafka_target): The Kafka target to write to.
        """
        self.__kafka_target = kafka_targ
        self.__lock = threading.Lock()

    def write(self, to_write: writable) -> None:
        """
        Writes the given data to the Kafka target.

        Args:
            to_write (writable): The data to write.

        Returns:
            None
        """
        with self.__lock:
            self.__kafka_target.write_to_kafka(json.dumps(to_write.to_json()))
