from .Writer import Writer
from .kafkaAdapter.KafkaTarget import KafkaTarget
#import asyncio
class KafkaWriter(Writer):
    #adapter
    #Cosi posso cambiare le librerie di invio, questa non cambia pero
    __kafka_target: KafkaTarget = None

    def __init__(self, kafka_target: KafkaTarget):
        self.__kafka_target = kafka_target

    def write(self, to_write: str) -> None:
        self.__kafka_target.write_to_kafka(to_write)
        #asyncio.run(self.__kafka_target.write_to_kafka(to_write))

