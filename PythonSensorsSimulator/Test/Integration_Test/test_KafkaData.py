# pylint: skip-file
import os
from datetime import datetime
import json
import pytest
import asyncio
from kafka import KafkaConsumer
from ...Model.Simulators.Coordinate import Coordinate
from ...Model.Simulators.Misurazione import Misurazione
from ...Model.Writers.KafkaWriter import KafkaWriter
from ...Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
from ...Model.AdapterMisurazione import AdapterMisurazione

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
def kafka_writer():
    adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
    kafka_writer = KafkaWriter(adapter_kafka)
    yield kafka_writer

@pytest.mark.asyncio
async def test_1_misurazione_kafka(kafka_consumer,kafka_writer):

    try:
        timestamp = datetime.now()
        to_send = Misurazione(timestamp, 4001, "temperature", Coordinate(45.39214, 11.859271), "test_kfk_1", "Arcella1")
        misurazione = AdapterMisurazione(to_send)
        kafka_writer.write(misurazione)
        kafka_writer.flush_kafka_producer()
        await asyncio.sleep(2)
        arrived = []
        for _ in kafka_consumer:
            #print(_.value)
            msg = AdapterMisurazione.from_json(json.loads(_.value))
            arrived.append(msg)
       
        assert to_send in arrived
    except Exception as e:
        pytest.fail(f"Failed to connect to kafka: {e}")

@pytest.mark.asyncio
async def test_multiple_misurazioni_kafka(kafka_consumer, kafka_writer):
    try:
        misurazioni = []
        data_to_send = 100
        timestamps =[]
        for i in range(data_to_send):
            timestamp = datetime.now()
            timestamps.append(timestamp)
            to_send = Misurazione(timestamp,600 + i, "test", Coordinate(45, 11), "test_kfk_multi", "Arcella")
            misurazione = AdapterMisurazione(to_send)
            misurazioni.append(to_send)
            kafka_writer.write(misurazione)
            kafka_writer.flush_kafka_producer()
        await asyncio.sleep(10)
        arrived = []
        for _ in kafka_consumer:
            #print(_.value)
            msg = AdapterMisurazione.from_json(json.loads(_.value))
            arrived.append(msg)
        for msg in misurazioni:
            assert msg in arrived
    except Exception as e:
        pytest.fail(f"Failed to connect to Kafka: {e}")
