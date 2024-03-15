# pylint: skip-file
import os
from datetime import datetime
import asyncio
import pytest
import clickhouse_connect

from ...Model.Simulators.coordinate import coordinate
from ...Model.Simulators.misurazione import misurazione
from ...Model.Writers.kafka_writer import kafka_writer
from ...Model.Writers.KafkaAdapter.kafka_confluent_adapter import kafka_confluent_adapter
from ...Model.adapter_misurazione import adapter_misurazione
from ...Model.Simulators.sensor_types import sensor_types

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")
topic_tmp = "temperature"
topic_umd = "humidity"
table_to_test = "healthScore"

@pytest.fixture(scope='module')
def clickhouse_client():
    client = clickhouse_connect.get_client(host='clickhouse', port=8123, database="innovacity")
    yield client
    client.close()

@pytest.fixture(scope='module')
def kafka_writer_tmp():
    adapter_kafka_tmp = kafka_confluent_adapter(topic_tmp, KAFKA_HOST, KAFKA_PORT)
    kafka_writer_tmp = kafka_writer(adapter_kafka_tmp)
    yield kafka_writer_tmp

@pytest.fixture(scope='module')
def kafka_writer_umd():
    adapter_kafka_umd = kafka_confluent_adapter(topic_umd, KAFKA_HOST, KAFKA_PORT)
    kafka_writer_umd = kafka_writer(adapter_kafka_umd)
    yield kafka_writer_umd

@pytest.mark.asyncio
async def test_heatlh_score_integration(clickhouse_client, kafka_writer_tmp, kafka_writer_umd):
    try:
        timestamp = datetime.now()

        tmp_sensor_data = [
            {"id": "HS_1_tmp", "cella": "HSTestCell", "timestamp": timestamp, "value": 25, "longitude": 11.859271, "latitude": 45.39214, "type": sensor_types.TEMPERATURE.value},
            {"id": "HS_2_tmp", "cella": "HSTestCell", "timestamp": timestamp, "value": 25, "longitude": 11.859271, "latitude": 45.39214, "type": sensor_types.TEMPERATURE.value},
            {"id": "HS_3_tmp", "cella": "HSTestCell", "timestamp": timestamp, "value": 25, "longitude": 11.859271, "latitude": 45.39214, "type": sensor_types.TEMPERATURE.value}
        ]

        umd_sensor_data = [
            {"id": "HS_1_umd", "cella": "HSTestCell", "timestamp": timestamp, "value": 50, "longitude": 11.859271, "latitude": 45.39214, "type": sensor_types.HUMIDITY.value},
            {"id": "HS_2_umd", "cella": "HSTestCell", "timestamp": timestamp, "value": 50, "longitude": 11.859271, "latitude": 45.39214, "type": sensor_types.HUMIDITY.value},
            {"id": "HS_3_umd", "cella": "HSTestCell", "timestamp": timestamp, "value": 50, "longitude": 11.859271, "latitude": 45.39214, "type": sensor_types.HUMIDITY.value}
        ]

        for data in tmp_sensor_data:
            misurazione = adapter_misurazione(
                misurazione(data["timestamp"], data["value"], data["type"], coordinate(data["latitude"],data["longitude"]), data["id"], data["cella"]))
            kafka_writer_tmp.write(misurazione)

        for data in umd_sensor_data:
            misurazione = adapter_misurazione(
                misurazione(data["timestamp"], data["value"], data["type"], coordinate(data["latitude"],data["longitude"]), data["id"], data["cella"]))
            kafka_writer_umd.write(misurazione)

        kafka_writer_tmp.flush_kafka_producer()
        kafka_writer_umd.flush_kafka_producer()

        query = f"SELECT * FROM innovacity.{table_to_test} where timestamp >= '{timestamp}' order by timestamp desc"

        result = clickhouse_client.query(query)
        iter = 0
        max_seconds_to_wait = 15
        intervallo_sleep = 0.5
        while (not result.result_rows) and (iter * intervallo_sleep < max_seconds_to_wait):
            await asyncio.sleep(intervallo_sleep)
            result = clickhouse_client.query(query)
            iter += 1

        expected_result = 0
        assert result.result_rows
        assert  float(result.result_rows[0][2]) == expected_result

    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")

