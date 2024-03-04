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



@pytest.mark.asyncio
async def test_1_misurazione():
    try:
        adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
        kafka_writer = KafkaWriter(adapter_kafka)
        misurazione = AdapterMisurazione(Misurazione('2022-02-28 10:20:37.206573', 4001, "Temperature", Coordinate(45.39214, 11.859271), "Tmp1", "Arcella1"))
        kafka_writer.write(misurazione)
        time.sleep(10)

        # Consuming the message from Kafka
        consumer = KafkaConsumer(test_topic, bootstrap_servers=f"{KAFKA_HOST}:{KAFKA_PORT}", auto_offset_reset='earliest', group_id=None)
        messages = consumer.poll(timeout_ms=10000)
        consumer.close()
        
        # Check if the message is received
        assert len(messages) > 0, "Message not received on Kafka"

        # Extracting and parsing the message
        received_message = next(iter(messages.values()))[0].value.decode('utf-8')
        received_json = json.loads(received_message)

        # Constructing the expected message
        expected_message = {
            "timestamp": '2022-02-28 10:20:37.206573',
            "id": 4001,
            "type": "Temperature",
            "coordinates": {"latitude": 45.39214, "longitude": 11.859271},
            "sensor_name": "Tmp1",
            "location_name": "Arcella1"
        }

        # Check if the received message is equal to the expected message
        assert received_json == expected_message, f"Received message {received_json} is not equal to expected message {expected_message}"

    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")
