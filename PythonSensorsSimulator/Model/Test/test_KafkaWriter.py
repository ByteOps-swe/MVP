import unittest
from unittest.mock import Mock, patch
from ..Writers.kafkaAdapter.KafkaTarget import KafkaTarget
from ..Writers.Writable import Writable
from ..Writers.KafkaWriter import KafkaWriter


class TestKafkaWriter(unittest.TestCase):

    def setUp(self):
        self.kafka_target = Mock(spec=KafkaTarget)
        self.kafka_writer = KafkaWriter(self.kafka_target)
        self.mock_writable = Mock(spec=Writable)

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
