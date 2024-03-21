# pylint: skip-file
import os
from datetime import datetime
import json
import pytest
import asyncio
from kafka import KafkaConsumer
from ...Model.Simulators.coordinate import coordinate
from ...Model.Simulators.misurazione import misurazione
from ...Model.Writers.kafka_writer import kafka_writer
from ...Model.Writers.KafkaAdapter.kafka_confluent_adapter import kafka_confluent_adapter
from ...Model.adapter_misurazione import adapter_misurazione

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")
test_topic = "test_kafka_only"

@pytest.fixture
def kafka_consumer():
        kafka_consumer = KafkaConsumer(test_topic,
            bootstrap_servers=f"{KAFKA_HOST}:{KAFKA_PORT}",
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id="test_id",
            value_deserializer=lambda x: x.decode('utf-8'),
            consumer_timeout_ms=10000)
        yield kafka_consumer

        kafka_consumer.close()

@pytest.fixture
def kafka_write():
    adapter_kafka = kafka_confluent_adapter(test_topic, KAFKA_HOST, KAFKA_PORT)
    kafka_write = kafka_writer(adapter_kafka)
    yield kafka_write

@pytest.mark.asyncio
async def test_1_misurazione_kafka(kafka_consumer, kafka_write):
    try:
        timestamp = datetime.now()
        to_send = misurazione(timestamp, 4001, "temperature", coordinate(45.39214, 11.859271), "test_kfk_1", "Arcella1")
        measure = adapter_misurazione(to_send)
        kafka_write.write(measure)
        kafka_write.flush_kafka_producer()
        await asyncio.sleep(2)
        arrived = []
        for _ in kafka_consumer:
            msg = adapter_misurazione.from_json(json.loads(_.value))
            arrived.append(msg)
       
        assert to_send in arrived
    except Exception as e:
        pytest.fail(f"Failed to connect to kafka: {e}")

@pytest.mark.asyncio
async def test_multiple_misurazioni_kafka(kafka_consumer, kafka_write):
    try:
        misurazioni = []
        data_to_send = 100
        timestamps =[]
        for i in range(data_to_send):
            timestamp = datetime.now()
            timestamps.append(timestamp)
            to_send = misurazione(timestamp,600 + i, "test", coordinate(45, 11), "test_kfk_multi", "Arcella")
            measure = adapter_misurazione(to_send)
            misurazioni.append(to_send)
            kafka_write.write(measure)
            kafka_write.flush_kafka_producer()
        await asyncio.sleep(10)
        arrived = []
        for _ in kafka_consumer:
            msg = adapter_misurazione.from_json(json.loads(_.value))
            arrived.append(msg)
        for msg in misurazioni:
            assert msg in arrived
    except Exception as e:
        pytest.fail(f"Failed to connect to Kafka: {e}")
