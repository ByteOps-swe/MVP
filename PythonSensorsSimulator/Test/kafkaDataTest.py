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
    kafka_consumer = KafkaConsumer(test_topic, bootstrap_servers=f"{KAFKA_HOST}:{KAFKA_PORT}", auto_offset_reset='earliest', group_id=None)
    yield kafka_consumer
    kafka_consumer.close()

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
        data_to_send = 100
        for i in range(data_to_send):
            to_send = Misurazione('2022-02-28 10:20:37.206573',600 + i, "test", Coordinate(45, 11), "Tmp1", "Arcella")
            misurazione = AdapterMisurazione(to_send)
            misurazioni.append(to_send)
            kafka_writer.write(misurazione)
            kafka_writer.flush_kafka_producer()
        time.sleep(5)
        arrived = []
        messages = kafka_consumer.poll(timeout_ms=10000)
        for i in range(len(next(iter(messages.values())))):
            msg_json = next(iter(messages.values()))[i].value.decode('utf-8')
            msg = AdapterMisurazione.from_json(json.loads(msg_json))
            arrived.append(msg)
            if msg in misurazioni:
                print(msg_json)
        for msg in misurazioni:
            assert msg in arrived
    except Exception as e:
        pytest.fail(f"Failed to connect to Kafka: {e}")

