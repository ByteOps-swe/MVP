# pylint: skip-file
import os
from datetime import datetime
from unittest.mock import Mock
import pytest
import asyncio
import clickhouse_connect

from ...Model.Simulators.Coordinate import Coordinate
from ...Model.Simulators.Misurazione import Misurazione
from ...Model.Writers.KafkaWriter import KafkaWriter
from ...Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
from ...Model.AdapterMisurazione import AdapterMisurazione

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

test_topic = "test"
table_to_test = "test"

@pytest.fixture(scope='module')
def clickhouse_client():
    client = clickhouse_connect.get_client(host='clickhouse', port=8123, database="innovacity")
    yield client
    client.close()

@pytest.fixture
def kafka_writer():
    adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
    kafka_writer = KafkaWriter(adapter_kafka)
    yield kafka_writer

@pytest.mark.asyncio
async def test_string_value(clickhouse_client,kafka_writer):
    try:
        timestamp = datetime.now()
        sensor_data = [
            {"id": "error_test_str_val","cella":"Arcella","timestamp":timestamp,"value": "$$$$","longitude": 11.859271,"latitude": 45.39214,"type": "Temperature"},
            {"id": "correct_test_str_val","cella":"Arcella","timestamp":timestamp,"value": 503,"longitude": 11.859271,"latitude": 45.39214,"type": "Temperature"}
        ]
        for data in sensor_data:
            misurazione = AdapterMisurazione(
                Misurazione(data["timestamp"], data["value"], data["type"], Coordinate(data["latitude"],data["longitude"]), data["id"], data["cella"]))
            kafka_writer.write(misurazione)
        kafka_writer.flush_kafka_producer()
        await asyncio.sleep(10)

        result = clickhouse_client.query(
            f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='{sensor_data[1]['id']}' and timestamp = '{sensor_data[1]['timestamp']}' LIMIT 1")
        assert float(result.result_rows[0][3]) == 503
        assert timestamp == result.result_rows[0][2]
        result = clickhouse_client.query(
             f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='{sensor_data[0]['id']}' and timestamp = '{sensor_data[0]['timestamp']}' LIMIT 1")
        assert not result.result_rows
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")

@pytest.mark.asyncio
async def test_dirty_timestamp(clickhouse_client,kafka_writer):
    try:
        mock_adapter_misurazione_corretta = Mock()
        mock_adapter_misurazione_corretta.to_json.return_value = {
            "timestamp": "2024-03-05 12:30:00.000000",
            "value": 25.50,
            "type": "tipo",
            "latitude": 123.45,
            "longitude": 67.89,
            "ID_sensore": "id_drt_time_correct",
            "cella": "cella"
        }
        mock_adapter_misurazione_sbagliata = Mock()
        mock_adapter_misurazione_sbagliata.to_json.return_value = {
            "timestamp": "$$$not_data",
            "value": 25.50,
            "type": "tipo",
            "latitude": 123.45,
            "longitude": 67.89,
            "ID_sensore": "id_drt_time_wrong",
            "cella": "cella"
        }
        kafka_writer.write(mock_adapter_misurazione_corretta) 
        kafka_writer.flush_kafka_producer()
        await asyncio.sleep(5)
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'id_drt_time_correct' LIMIT 1")
        assert float(result.result_rows[0][3]) == 25.5
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'id_drt_time_wrong' LIMIT 1")
        assert not result.result_rows
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")

@pytest.mark.asyncio
async def test_dirty_coordinates(clickhouse_client,kafka_writer):
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
        kafka_writer.write(mock_adapter_misurazione_corretta)
        kafka_writer.flush_kafka_producer()
        await asyncio.sleep(10)
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'ID_drty_coord_right' and timestamp = '{str(timestamp)}' LIMIT 1")
        assert float(result.result_rows[0][3]) == 25.5
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'ID_drty_coord_wrong' and timestamp = '{str(timestamp)}' LIMIT 1")
        assert not result.result_rows
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")
