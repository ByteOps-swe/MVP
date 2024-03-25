import threading
from .writer_strategy import writer_strategy
from .KafkaAdapter.kafka_target import kafka_target
from .writable import writable

class kafka_writer(writer_strategy):

    def __init__(self, kafka_targ: kafka_target):
        self.__kafka_target = kafka_targ
        self.__lock = threading.Lock()

    def write(self, to_write: writable) -> None:
        with self.__lock:
            self.__kafka_target.write_to_kafka(to_write.to_json())

    def flush_kafka_producer(self):
        self.__kafka_target.flush_kafka_producer()
