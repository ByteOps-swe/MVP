from .KafkaTarget import KafkaTarget
from confluent_kafka import Producer, KafkaException


def acked(err, msg):
    if err is not None:
        print("Fallimento nella consegna del messaggio: %s: %s" %
              (str(msg), str(err)))

class KafkaConfluentAdapter(KafkaTarget):
    def __init__(self,topic:str, ip: str = "localhost", port: str = "9092"):
        self.__producer = None
        self.__topic = topic
        self.__configure_producer(ip, port)

    def __configure_producer(self, ip: str, port: str) -> None:
        config = {'bootstrap.servers': ip + ':' + port}
        try:
            self.__producer = Producer(config)
        except KafkaException as e:
            print(f"Errore nella creazione del producer: {e}")

    def write_to_kafka(self, data: str) -> None:
        try:
            self.__producer.produce(self.__topic, value=data, callback=acked)
            self.__producer.poll(1)
        except KafkaException as e:
            print(f"Errore durante la scrittura in Kafka: {e}")