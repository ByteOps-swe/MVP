from .Writer import Writer
from .KafkaWriter import KafkaWriter
from .StdoutWriter import StdoutWriter
from .ListWriter import ListWriter
from .kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter

#pattern composite https://refactoring.guru/design-patterns/composite
class CompositeWriter(Writer):

    def __init__(self):
        self._writers = []

    def add_writer(self, writer):
        if not isinstance(writer, Writer):
            raise ValueError("Object is not a Writer instance")
        self._writers.append(writer)
        return self

    def add_kafkaConfluent_writer(self, topic:str,host,port):
        self.add_writer(KafkaWriter(KafkaConfluentAdapter(topic,host,port)))
        return self

    def add_stdOut_writer(self):
        self.add_writer(StdoutWriter())
        return self

    def add_list_writer(self, writer_list : ListWriter ):
        self.add_writer(writer_list)
        return self

    def remove_writer(self, writer):
        self._writers.remove(writer)

    def write(self, to_write):
        for writer in self._writers:
            writer.write(to_write)
