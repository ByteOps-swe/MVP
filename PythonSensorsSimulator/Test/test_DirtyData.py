import os
import time
from datetime import datetime
from unittest.mock import Mock
import pytest
import clickhouse_connect

from ..Model.Simulators.Coordinate import Coordinate
from ..Model.Simulators.Misurazione import Misurazione
from ..Model.Writers.KafkaWriter import KafkaWriter
from ..Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
from ..Model.AdapterMisurazione import AdapterMisurazione

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

test_topic = "test"
table_to_test = "test"

@pytest.fixture(scope='module')
def clickhouse_client():
    # Set up ClickHouse client
    client = clickhouse_connect.get_client(host='clickhouse', port=8123, database="innovacity")
    yield client
    # Teardown: Close connection after all tests in the module have run
    client.close()

@pytest.mark.asyncio
async def test_string_value(clickhouse_client):
    try:
        adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
        kafka_writer = KafkaWriter(adapter_kafka)
        timestamp = datetime.now()
        misurazione = AdapterMisurazione(
            Misurazione(timestamp, "$$$$", "Temperature", Coordinate(45.39214, 11.859271), "error_test", "Arcella"))
        kafka_writer.write(misurazione)
        misurazione = AdapterMisurazione(
            Misurazione(timestamp, 503, "Temperature", Coordinate(45.39214, 11.859271), "correct_test", "Arcella"))
        kafka_writer.write(misurazione)
        kafka_writer.flush_kafka_producer()
        time.sleep(5)
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='correct_test' and timestamp = '{str(timestamp)}' LIMIT 1")
        assert float(result.result_rows[0][3]) == 503
        str(timestamp)[:22] == str(result.result_rows[0][2])[:22]
        result = clickhouse_client.query(
            f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='error_test' and timestamp = '{str(timestamp)}' LIMIT 1")
        assert not result.result_rows
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")

@pytest.mark.asyncio
async def test_dirty_timestamp(clickhouse_client):
    try:
        mock_adapter_misurazione_corretta = Mock()
        mock_adapter_misurazione_corretta.to_json.return_value = {
            "timestamp": "2024-03-05 12:30:00.000000",
            "value": 25.50,
            "type": "tipo",
            "latitude": 123.45,
            "longitude": 67.89,
            "ID_sensore": "sensore",
            "cella": "cella"
        }
        mock_adapter_misurazione_sbagliata = Mock()
        mock_adapter_misurazione_sbagliata.to_json.return_value = {
            "timestamp": "$$$not_data",
            "value": 25.50,
            "type": "tipo",
            "latitude": 123.45,
            "longitude": 67.89,
            "ID_sensore": "sensore_unique1",
            "cella": "cella"
        }
        adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
        kafka_writer = KafkaWriter(adapter_kafka)
        kafka_writer.write(mock_adapter_misurazione_corretta) 
        kafka_writer.flush_kafka_producer()
        time.sleep(5)
        result = clickhouse_client.query(f'SELECT * FROM innovacity.{table_to_test} where value =25.5 LIMIT 1')
        assert float(result.result_rows[0][3]) == 25.5
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'sensore_unique1' LIMIT 1")
        assert not result.result_rows
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")

@pytest.mark.asyncio
async def test_dirty_coordinates(clickhouse_client):
    try:
        timestamp = datetime.now()
        mock_adapter_misurazione_corretta = Mock()
        mock_adapter_misurazione_corretta.to_json.return_value = {
            "timestamp": str(timestamp),
            "value": 25.50,
            "type": "tipo",
            "latitude": 123.45,
            "longitude": 67.89,
            "ID_sensore": "ID_drty_coord_right",
            "cella": "cella"
        }
        mock_adapter_misurazione_sbagliata = Mock()
        mock_adapter_misurazione_sbagliata.to_json.return_value = {
            "timestamp": str(timestamp),
            "value": 25.50,
            "type": "tipo",
            "latitude": "/$$!",
            "longitude": "ciaoNo2$",
            "ID_sensore": "ID_drty_coord_wrong",
            "cella": "cella"
        }
        adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
        kafka_writer = KafkaWriter(adapter_kafka)
        kafka_writer.write(mock_adapter_misurazione_corretta)
        kafka_writer.flush_kafka_producer()
        time.sleep(5)
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'ID_drty_coord_right' and timestamp = '{str(timestamp)}' LIMIT 1")
        assert float(result.result_rows[0][3]) == 25.5
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'ID_drty_coord_wrong' and timestamp = '{str(timestamp)}' LIMIT 1")
        assert not result.result_rows
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")
