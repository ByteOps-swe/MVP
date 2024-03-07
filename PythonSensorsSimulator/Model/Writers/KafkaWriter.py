import json
from threading import Lock
from .Writer import Writer
from .kafkaAdapter.KafkaTarget import KafkaTarget
from .Writable import Writable

class KafkaWriter(Writer):

    __lock: Lock = Lock()

    def __init__(self, kafka_target: KafkaTarget):
        self.__kafka_target = kafka_target

    async def write(self, to_write: Writable) -> None:
        with self.__lock:
            self.__kafka_target.write_to_kafka(json.dumps(to_write.to_json()))

    def flush_kafka_producer(self):
        self.__kafka_target.flush_kafka_producer()
