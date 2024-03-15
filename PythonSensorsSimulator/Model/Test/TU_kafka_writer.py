import unittest
from unittest.mock import Mock, patch
from ..Writers.KafkaAdapter import kafka_target
from ..Writers import writable
from ..Writers import kafka_writer


class TU_kafka_writer(unittest.TestCase):

    def set_up(self):
        self.kafka_target = Mock(spec=kafka_target)
        self.kafka_writer = kafka_writer(self.kafka_target)
        self.mock_writable = Mock(spec=writable)

    def test_write(self):
        with patch('json.dumps') as mock_json_dumps:
            self.kafka_writer.write(self.mock_writable)
            mock_json_dumps.assert_called_once_with(self.mock_writable.to_json())
            self.kafka_target.write_to_kafka.assert_called_once_with(mock_json_dumps.return_value)

    def test_flush_kafka_producer(self):
        self.kafka_writer.flush_kafka_producer()
        self.kafka_target.flush_kafka_producer.assert_called_once()


if __name__ == '__main__':
    unittest.main()
