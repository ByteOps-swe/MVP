import unittest
from unittest.mock import Mock, patch
from ..HealthStateModel.Writers.KafkaAdapter.kafka_target import kafka_target
from ..HealthStateModel.Writers.writable import writable
from ..HealthStateModel.Writers.kafka_writer import kafka_writer


class TU_kafka_writer(unittest.TestCase):

    def setUp(self):
        self.kafka_target = Mock(spec=kafka_target)
        self.kafka_writer = kafka_writer(self.kafka_target)
        self.mock_writable = Mock(spec=writable)

    def test_write(self):
        with patch.object(self.mock_writable, 'to_json') as mock_to_json:
            self.kafka_writer.write(self.mock_writable)
            mock_to_json.assert_called_once()
            self.kafka_target.write_to_kafka.assert_called_once()

    def test_flush_kafka_producer(self):
        self.kafka_writer.flush_kafka_producer()
        self.kafka_target.flush_kafka_producer.assert_called_once()


if __name__ == '__main__':
    unittest.main()
