import json
from confluent_kafka import Producer, KafkaException
from .KafkaTarget import KafkaTarget
from avro import schema

import avro.schema  # Import the schema class
from confluent_kafka.avro.cached_schema_registry_client import CachedSchemaRegistryClient

def acked(err, msg):
    if err is not None:
        print(f"Fallimento nella consegna del messaggio: {msg}: {err}")

class KafkaConfluentAdapter(KafkaTarget):
    def __init__(self, topic: str, ip: str = "kafka", port: str = "9092"):
        self.__topic = topic
        self.__schema_registry_client =CachedSchemaRegistryClient(url="http://schema_registry:8081")
        self.__schema = self.__schema_registry_client.get_latest_schema("temperature")[1]
        print(str(self.__schema))
        config = {'bootstrap.servers': ip + ':' + port}
        try:
            self.__producer = Producer(config)
        except KafkaException as e:
            print(f"Errore nella creazione del producer: {e}")

    def write_to_kafka(self, data) -> None:
        try:
            try:
                avro.validate(schema.parse(str(self.__schema)), data)
            except avro.ValidationError as e:
                print(f"Errore di convalida: {e}")
            self.__producer.produce(self.__topic, value=json.dumps(data), callback=acked)
            self.__producer.flush()
            self.__producer.poll(1)
        except KafkaException as e:
            print(f"Errore durante la scrittura in Kafka: {e}")

    def flush_kafka_producer(self):
        try:
            self.__producer.flush()
        except Exception as e:
            print(f"Error while flushing Kafka producer: {e}")
