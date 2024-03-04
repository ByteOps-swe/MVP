import pytest
import os
import json
from kafka import KafkaConsumer
from .Model.Simulators.Coordinate import Coordinate
from .Model.Simulators.Misurazione import Misurazione
from .Model.Writers.KafkaWriter import KafkaWriter
from .Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
from .Model.AdapterMisurazione import AdapterMisurazione
import time

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

test_topic = "test_kafka_topic"

@pytest.fixture
def kafka_consumer():
    consumer = KafkaConsumer(test_topic, bootstrap_servers=f"{KAFKA_HOST}:{KAFKA_PORT}", auto_offset_reset='earliest', group_id=None)
    yield consumer
    consumer.close()

@pytest.fixture
def kafka_writer():
    adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
    kafka_writer = KafkaWriter(adapter_kafka)
    yield kafka_writer

@pytest.mark.asyncio
async def test_1_misurazione(kafka_consumer, kafka_writer):
    try:
        to_send = Misurazione('2022-02-28 10:20:37.206573', 4001, "Temperature", Coordinate(45.39214, 11.859271), "Tmp1", "Arcella1")
        misurazione = AdapterMisurazione(to_send)
        kafka_writer.write(misurazione)
        kafka_writer.flush_kafka_producer()
        time.sleep(2)

        # Consuming the message from Kafka
        messages = kafka_consumer.poll(timeout_ms=10000)
        
        # Check if the message is received
        assert len(messages) > 0, "Message not received on Kafka"

        # Extracting and parsing the message
        received_message = next(iter(messages.values()))[0].value.decode('utf-8')
        received_json = json.loads(received_message)
        arrived = AdapterMisurazione.from_json(received_json)

        assert arrived == to_send

    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")
