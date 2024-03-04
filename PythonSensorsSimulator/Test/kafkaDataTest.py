import pytest
import os
import json
from kafka import KafkaConsumer
from ..Model.Simulators.Coordinate import Coordinate
from ..Model.Simulators.Misurazione import Misurazione
from ..Model.Writers.KafkaWriter import KafkaWriter
from ..Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
from ..Model.AdapterMisurazione import AdapterMisurazione
import time

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

test_topic = "test"

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
        to_send = Misurazione('2022-02-28 10:20:37.206573', 4001, "temperature", Coordinate(45.39214, 11.859271), "Tmp1", "Arcella1")
        misurazione = AdapterMisurazione(to_send)
        kafka_writer.write(misurazione)
        kafka_writer.flush_kafka_producer()
        time.sleep(2)
        messages = kafka_consumer.poll(timeout_ms=10000)
        assert len(messages) > 0, "Message not received on Kafka"
        received_message = next(iter(messages.values()))[0].value.decode('utf-8')
        received_json = json.loads(received_message)
        arrived = AdapterMisurazione.from_json(received_json)
        assert arrived == to_send

    except Exception as e:
        pytest.fail(f"Failed to connect to kafka: {e}")

@pytest.mark.asyncio
async def test_multiple_misurazioni(kafka_consumer, kafka_writer):
    try:
        misurazioni = []
        for i in range(100):
            to_send = Misurazione(f'2022-02-28 10:20:37.206573{i}', 4001 + i, "test", Coordinate(45.39214 + i, 11.859271 + i), f"Tmp{i}", f"Arcella{i}")
            misurazione = AdapterMisurazione(to_send)
            misurazioni.append(to_send)
            kafka_writer.write(misurazione)

        kafka_writer.flush_kafka_producer()
        time.sleep(10)  # Increase if necessary

        # Consuming the messages from Kafka
        messages = kafka_consumer.poll(timeout_ms=10000)
        print(len(messages))
        assert len(messages) == 100, "100 messages not received on Kafka"

        # Extracting and parsing the messages
        received_messages = [json.loads(msg.value.decode('utf-8')) for msg in messages.values()]
        received_misurazioni = [AdapterMisurazione.from_json(msg) for msg in received_messages]

        # Check if all the sent misurazioni have arrived
        for sent_misurazione in misurazioni:
            assert sent_misurazione in received_misurazioni, f"Sent misurazione {sent_misurazione} not received on Kafka"

    except Exception as e:
        pytest.fail(f"Failed to connect to Kafka: {e}")

