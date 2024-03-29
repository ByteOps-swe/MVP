import os
import unittest
from unittest.mock import MagicMock, patch
from ..HealthStateModel.Writers.KafkaAdapter.kafka_confluent_adapter import kafka_confluent_adapter

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")
test_topic = "test"
table_to_test = "test"

class TestKafkaConfluentAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_producer = MagicMock()
        self.mock_schema_registry_client = MagicMock()
        self.adapter = kafka_confluent_adapter(test_topic, KAFKA_HOST, KAFKA_PORT)
        self.adapter._kafka_confluent_adapter__producer = self.mock_producer
        self.adapter._kafka_confluent_adapter__schema_registry_client = self.mock_schema_registry_client

    def test_write_to_kafka_valid_data(self):
        self.mock_schema_registry_client.get_latest_schema.return_value = (1, "test_schema")
        with patch('builtins.validate') as mock_validate:
            mock_validate.return_value = True
            self.adapter.write_to_kafka("test_data")
            self.mock_producer.produce.assert_called_once_with("test_topic", value='test_data', callback=self.adapter.callback)
            self.mock_producer.poll.assert_called_once_with(1)

    def test_write_to_kafka_invalid_data(self):
        self.mock_schema_registry_client.get_latest_schema.return_value = (1, "test_schema")
        with patch('builtins.validate') as mock_validate:
            mock_validate.return_value = False
            self.adapter.write_to_kafka("invalid_data")
            self.mock_producer.produce.assert_not_called()
            self.mock_producer.poll.assert_not_called()

    def test_flush_kafka_producer(self):
        self.adapter.flush_kafka_producer()
        self.mock_producer.flush.assert_called_once()

if __name__ == '__main__':
    unittest.main()