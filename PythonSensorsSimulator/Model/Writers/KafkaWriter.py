from .Writer import Writer
from .kafkaAdapter.KafkaTarget import KafkaTarget
import json
from threading import Lock
from ..Simulators.Misurazione import Misurazione

class KafkaWriter(Writer):
    __kafka_target: KafkaTarget = None
    __lock: Lock = Lock()  # Lock per garantire l'accesso thread-safe al KafkaTarget

    def __init__(self, kafka_target: KafkaTarget):
        self.__kafka_target = kafka_target

    def write(self, to_write: Misurazione) -> None:
        with self.__lock:  # Acquisisce il lock prima di eseguire l'operazione di scrittura su KafkaTarget
            self.__kafka_target.write_to_kafka(json.dumps(to_write.to_json()))
