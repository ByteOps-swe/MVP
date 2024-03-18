from confluent_kafka import Producer, KafkaException
from confluent_kafka.avro.cached_schema_registry_client import CachedSchemaRegistryClient
from avro.io import validate
from .kafka_target import kafka_target

def acked(err, msg):
    if err is not None:
        print(f"Fallimento nella consegna del messaggio: {msg}: {err}")

class kafka_confluent_adapter(kafka_target):
    def __init__(self, topic: str, ip: str = "kafka", port: int = 9092, schema_registry_url: str = "http://schema_registry:8081", schema_name: str = "misurazioneSalute"):
        self.__topic = topic
        self.__schema_registry_client =CachedSchemaRegistryClient(url=schema_registry_url)
        self.__schema = self.__schema_registry_client.get_latest_schema(schema_name)[1]
        config = {'bootstrap.servers': ip + ':' + str(port)}
        try:
            self.__producer = Producer(config)
        except KafkaException as e:
            print(f"Errore nella creazione del producer: {e}")

    def write_to_kafka(self, data: str) -> None:
        try:
            if validate(self.__schema, data):
                self.__producer.produce(self.__topic, value=data, callback=acked)
                self.__producer.poll(1)
        except KafkaException as e:
            print(f"Errore durante la scrittura in Kafka: {e}")

    def flush_kafka_producer(self):
        try:
            self.__producer.flush()
        except Exception as e:
            print(f"Error while flushing Kafka producer: {e}")
