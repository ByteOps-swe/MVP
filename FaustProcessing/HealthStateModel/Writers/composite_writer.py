from .writer import writer
from .kafka_writer import kafka_writer
from .std_out_writer import std_out_writer
from .KafkaAdapter.kafka_confluent_adapter import kafka_confluent_adapter
#pattern composite https://refactoring.guru/design-patterns/composite

class composite_writer(writer):

    def __init__(self):
        self._writers = []

    def add_writer(self, writ):
        if not isinstance(writ, writer):
            raise ValueError("Object is not a writer instance")
        self._writers.append(writ)
        return self

    def add_kafka_confluent_writer(self, topic:str, host:str, port, schema_registry_url:str):
        self.add_writer(kafka_writer(kafka_confluent_adapter(topic, host, port, schema_registry_url)))
        return self

    def add_std_out_writer(self):
        self.add_writer(std_out_writer())
        return self

    def remove_writer(self, writ):
        self._writers.remove(writ)

    def write(self, to_write):
        for writ in self._writers:
            writ.write(to_write)
