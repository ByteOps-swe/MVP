from .Writer import Writer
from confluent_kafka import Producer, KafkaException


def acked(err, msg):
    if err is not None:
        print("Fallimento nella consegna del messaggio: %s: %s" %
              (str(msg), str(err)))


class KafkaWriter(Writer):
    __producer: Producer = None
    __topic: str = None

    def __init__(self, topic: str, ip: str = "localhost", port: str = "9092"):
        config = {'bootstrap.servers': ip + ':' + port}
        self.__topic = topic
        try:
            self.__producer = Producer(config)
        except KafkaException as e:
            print(f"Errore nella creazione del producer: {e}")

    def write(self, to_write: str) -> None:
        self.__producer.produce(self.__topic, value=to_write, callback=acked)
        self.__producer.poll(1)
