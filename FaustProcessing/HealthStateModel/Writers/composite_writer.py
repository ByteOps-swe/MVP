from .writer import writer
from .kafka_writer import kafka_writer
from .std_out_writer import std_out_writer
from .KafkaAdapter.kafka_confluent_adapter import kafka_confluent_adapter
#pattern composite https://refactoring.guru/design-patterns/composite
class composite_writer(writer):
    """
    A class that represents a composite writer, which combines multiple writers into one.

    Attributes:
        _writers (list): A list of writer objects.

    Methods:
        add_writer(writer): Adds a writer to the composite writer.
        add_kafka_confluent_writer(topic, host, port): Adds a KafkaConfluentWriter to the composite writer.
        add_std_out_writer(): Adds a std_out_writer to the composite writer.
        remove_writer(writer): Removes a writer from the composite writer.
        write(to_write): Writes the given data using all the writers in the composite writer.
    """

    def __init__(self):
        self._writers = []

    def add_writer(self, writ):
        """
        Adds a writer to the composite writer.

        Args:
            writer (writer): The writer object to be added.

        Returns:
            composite_writer: The composite writer object.
        """
        if not isinstance(writ, writer):
            raise ValueError("Object is not a writer instance")
        self._writers.append(writ)
        return self

    def add_kafka_confluent_writer(self, topic:str, host:str, port:int):
        """
        Adds a KafkaConfluentWriter to the composite writer.

        Args:
            topic (str): The Kafka topic to write to.
            host (str): The Kafka host.
            port (int): The Kafka port.

        Returns:
            composite_writer: The composite writer object.
        """
        self.add_writer(kafka_writer(kafka_confluent_adapter(topic, host, port)))
        return self

    def add_std_out_writer(self):
        """
        Adds a std_out_writer to the composite writer.

        Returns:
            composite_writer: The composite writer object.
        """
        self.add_writer(std_out_writer())
        return self

    def remove_writer(self, writ):
        """
        Removes a writer from the composite writer.

        Args:
            writer (writer): The writer object to be removed.
        """
        self._writers.remove(writ)

    def write(self, to_write):
        """
        Writes the given data using all the writers in the composite writer.

        Args:
            to_write: The data to be written.
        """
        for writ in self._writers:
            writ.write(to_write)
