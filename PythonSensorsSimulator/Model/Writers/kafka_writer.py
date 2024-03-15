import json
from threading import Lock
from .writer import writer
from .KafkaAdapter.kafka_target import kafka_target
from .writable import writable

class kafka_writer(writer):

    __lock: Lock = Lock()

    def __init__(self, kafka_target: kafka_target):
        self.__kafka_target = kafka_target

    def write(self, to_write: writable) -> None:
        with self.__lock:
            self.__kafka_target.write_to_kafka(json.dumps(to_write.to_json()))

    def flush_kafka_producer(self):
        self.__kafka_target.flush_kafka_producer()
