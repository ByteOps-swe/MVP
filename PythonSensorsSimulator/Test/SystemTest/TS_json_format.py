# pylint: skip-file
import os
from datetime import datetime
from unittest.mock import Mock
import pytest
import asyncio

import clickhouse_connect
from ...Model.Writers import kafka_writer
from ...Model.Writers.KafkaAdapter import kafka_confluent_adapter

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
    kafka_writer = kafka_writer(adapter_kafka)
    yield kafka_writer
    
@pytest.mark.asyncio
async def test_missing_data_field(clickhouse_client,kafka_writer):
    try:
        mock_adapter_misurazione_corretta = Mock()
        mock_adapter_misurazione_corretta.to_json.return_value = {
            "timestamp": "2024-03-05 12:30:00.000000",
            "value": 25.50,
            "type": "tipo",
            "latitude": 123.45,
            "longitude": 67.89,
            "ID_sensore": "id_json_format_correct1",
            "cella": "cella"
        }
        mock_adapter_misurazione_sbagliata = Mock()
        mock_adapter_misurazione_sbagliata.to_json.return_value = {
            "timestamp": "2024-03-05 12:30:00.000000",
            "value": 25.50,
            "type": "tipo",
            "latitude": 123.45,
            "longitude": 67.89,
            "ID_sensore": "id_json_time_wrong1",
        }
        kafka_writer.write(mock_adapter_misurazione_corretta) 
        kafka_writer.flush_kafka_producer()
        await asyncio.sleep(10)
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'id_json_format_correct1' LIMIT 1")
        print(result.result_rows[0][3])
        assert float(result.result_rows[0][3]) == 25.5
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'id_json_format_wrong1' LIMIT 1")
        print(result.result_rows)
        assert not result.result_rows
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")
        
@pytest.mark.asyncio
async def test_wrong_field_order(clickhouse_client,kafka_writer):
    try:
        mock_adapter_misurazione_corretta = Mock()
        mock_adapter_misurazione_corretta.to_json.return_value = {
            "timestamp": "2024-03-05 12:30:00.000000",
            "value": 25.50,
            "type": "tipo",
            "latitude": 123.45,
            "longitude": 67.89,
            "ID_sensore": "id_json_format_correct2",
            "cella": "cella"
        }
        mock_adapter_misurazione_sbagliata = Mock()
        mock_adapter_misurazione_sbagliata.to_json.return_value = {
            "timestamp": "2024-03-05 12:30:00.000000",
            "value": 25.50,
            "latitude": 123.45,
            "type": "tipo",
            "ID_sensore": "id_json_format_wrong2",
            "longitude": 67.89,
            "cella": "cella"
        }
        kafka_writer.write(mock_adapter_misurazione_corretta) 
        kafka_writer.flush_kafka_producer()
        await asyncio.sleep(10)
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'id_json_format_correct2' LIMIT 1")
        print(result.result_rows[0][3])
        assert float(result.result_rows[0][3]) == 25.5
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore = 'id_json_format_wrong2' LIMIT 1")
        print(result.result_rows)
        assert not result.result_rows
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")

#Aggiungi test per un campo in piu'