# pylint: skip-file
import os
from datetime import datetime
import asyncio
import pytest
import clickhouse_connect

from ...Model.Simulators.Coordinate import Coordinate
from ...Model.Simulators.Misurazione import Misurazione
from ...Model.Writers.KafkaWriter import KafkaWriter
from ...Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
from ...Model.AdapterMisurazione import AdapterMisurazione

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")
test_topic = "dust_PM10"
table_to_test = "dust_PM10"

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
async def test_outOfBound_misurazione_tmp(clickhouse_client, kafka_writer):
    try:
        timestamp = datetime.now()
        low_bound_limit = 0
        upper_bound_limit = 150
        sensor_data = [
            {"id": "Id_1_tmp_correct_ofb", "cella": "Arcella", "timestamp": timestamp, "value": 50, "longitude": 11.859271, "latitude":45.39214, "type": "Dust_PM10"},
            {"id": "Id_1_tmp_error_ofb", "cella": "Arcella", "timestamp": timestamp, "value": 200, "longitude": 11.859271, "latitude":45.39214, "type": "Dust_PM10"},
            {"id": "Id_2_tmp_error_ofb", "cella": "Arcella", "timestamp": timestamp, "value": -10, "longitude": 11.859271, "latitude":45.39214, "type": "Dust_PM10"}
        ]

        for data in sensor_data:
            misurazione = AdapterMisurazione(
                Misurazione(data["timestamp"], data["value"], data["type"], Coordinate(data["latitude"],data["longitude"]), data["id"], data["cella"]))
            kafka_writer.write(misurazione)

        kafka_writer.flush_kafka_producer()
        await asyncio.sleep(5)

        for data in sensor_data:
            result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='{data['id']}' and timestamp = '{data['timestamp']}' LIMIT 1")
            if(data["value"] >= low_bound_limit and data["value"] <= upper_bound_limit):
                assert result.result_rows
                assert result.result_rows[0][0] == data["id"]
                assert result.result_rows[0][1] == data["cella"]
                assert str(timestamp)[:19] == str(result.result_rows[0][2])[:19]
                assert float(result.result_rows[0][3]) == data["value"]
                assert result.result_rows[0][4] == 45.39214
                assert result.result_rows[0][5] == 11.859271
            else:
                assert not result.result_rows

    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")

