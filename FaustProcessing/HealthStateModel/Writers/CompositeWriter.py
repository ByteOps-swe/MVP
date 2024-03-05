from .Writer import Writer
from .KafkaWriter import KafkaWriter
from .StdoutWriter import StdoutWriter
from .kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
#pattern composite https://refactoring.guru/design-patterns/composite
class CompositeWriter(Writer):
    """
    A class that represents a composite writer, which combines multiple writers into one.

    Attributes:
        _writers (list): A list of Writer objects.

    Methods:
        add_writer(writer): Adds a writer to the composite writer.
        add_kafkaConfluent_writer(topic, host, port): Adds a KafkaConfluentWriter to the composite writer.
        add_stdOut_writer(): Adds a StdoutWriter to the composite writer.
        remove_writer(writer): Removes a writer from the composite writer.
        write(to_write): Writes the given data using all the writers in the composite writer.
    """

    def __init__(self):
        self._writers = []

    def add_writer(self, writer):
        """
        Adds a writer to the composite writer.

        Args:
            writer (Writer): The writer object to be added.

        Returns:
            CompositeWriter: The composite writer object.
        """
        if not isinstance(writer, Writer):
            raise ValueError("Object is not a Writer instance")
        self._writers.append(writer)
        return self

    def add_kafkaConfluent_writer(self, topic:str, host:str, port:int):
        """
        Adds a KafkaConfluentWriter to the composite writer.

        Args:
            topic (str): The Kafka topic to write to.
            host (str): The Kafka host.
            port (int): The Kafka port.

        Returns:
            CompositeWriter: The composite writer object.
        """
        self.add_writer(KafkaWriter(KafkaConfluentAdapter(topic, host, port)))
        return self

    def add_stdOut_writer(self):
        """
        Adds a StdoutWriter to the composite writer.

        Returns:
            CompositeWriter: The composite writer object.
        """
        self.add_writer(StdoutWriter())
        return self

    def remove_writer(self, writer):
        """
        Removes a writer from the composite writer.

        Args:
            writer (Writer): The writer object to be removed.
        """
        self._writers.remove(writer)

    def write(self, to_write):
        """
        Writes the given data using all the writers in the composite writer.

        Args:
            to_write: The data to be written.
        """
        for writer in self._writers:
            writer.write(to_write)
