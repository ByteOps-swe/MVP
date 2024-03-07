from confluent_kafka import Producer, KafkaException
from .KafkaTarget import KafkaTarget

#Adattatore per la l'invio tramite libreria confluent kafka
def acked(err, msg):
    if err is not None:
        print(f"Fallimento nella consegna del messaggio: {msg}: {err}")

class KafkaConfluentAdapter(KafkaTarget):
    def __init__(self, topic: str, ip: str = "kafka", port: str = "9092"):
        self.__topic = topic
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

    def flush_kafka_producer(self):
        try:
            self.__producer.flush()
        except Exception as e:
            print(f"Error while flushing Kafka producer: {e}")
