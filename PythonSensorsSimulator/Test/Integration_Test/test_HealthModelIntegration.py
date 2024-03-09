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
from ...Model.Simulators.SensorTypes import SensorTypes

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")
topic_tmp = "temperature"
topic_umd = "umidity"
table_to_test = "healthScore"

@pytest.fixture(scope='module')
def clickhouse_client():
    client = clickhouse_connect.get_client(host='clickhouse', port=8123, database="innovacity")
    yield client
    client.close()

@pytest.fixture(scope='module')
def kafka_writer_tmp():
    adapter_kafka_tmp = KafkaConfluentAdapter(topic_tmp, KAFKA_HOST, KAFKA_PORT)
    kafka_writer_tmp = KafkaWriter(adapter_kafka_tmp)
    yield kafka_writer_tmp

@pytest.fixture(scope='module')
def kafka_writer_umd():
    adapter_kafka_umd = KafkaConfluentAdapter(topic_umd, KAFKA_HOST, KAFKA_PORT)
    kafka_writer_umd = KafkaWriter(adapter_kafka_umd)
    yield kafka_writer_umd

@pytest.mark.asyncio
async def test_heatlh_score_integration(clickhouse_client,kafka_writer_tmp,kafka_writer_umd):
    try:
        timestamp = datetime.now()

        tmp_sensor_data = [
            {"id": "HS_1_tmp","cella":"HSTestCell","timestamp":timestamp,"value": 25,"longitude": 11.859271,"latitude": 45.39214,"type": SensorTypes.TEMPERATURE.value},
            {"id": "HS_1_tmp","cella":"HSTestCell","timestamp":timestamp,"value": 25,"longitude": 11.859271,"latitude": 45.39214,"type": SensorTypes.TEMPERATURE.value},
            {"id": "HS_2_tmp","cella":"HSTestCell","timestamp":timestamp,"value": 25,"longitude": 11.859271,"latitude": 45.39214,"type": SensorTypes.TEMPERATURE.value}
        ]

        umd_sensor_data = [
            {"id": "HS_1_umd","cella":"HSTestCell","timestamp":timestamp,"value": 50,"longitude": 11.859271,"latitude": 45.39214,"type": SensorTypes.HUMIDITY.value},
            {"id": "HS_1_umd","cella":"HSTestCell","timestamp":timestamp,"value": 50,"longitude": 11.859271,"latitude": 45.39214,"type": SensorTypes.HUMIDITY.value},
            {"id": "HS_2_umd","cella":"HSTestCell","timestamp":timestamp,"value": 50,"longitude": 11.859271,"latitude": 45.39214,"type": SensorTypes.HUMIDITY.value}
        ]

        for data in tmp_sensor_data:
            misurazione = AdapterMisurazione(
                Misurazione(data["timestamp"], data["value"], data["type"], Coordinate(data["latitude"],data["longitude"]), data["id"], data["cella"]))
            kafka_writer_tmp.write(misurazione)

        for data in umd_sensor_data:
            misurazione = AdapterMisurazione(
                Misurazione(data["timestamp"], data["value"], data["type"], Coordinate(data["latitude"],data["longitude"]), data["id"], data["cella"]))
            kafka_writer_umd.write(misurazione)

        kafka_writer_tmp.flush_kafka_producer()
        kafka_writer_umd.flush_kafka_producer()

        await asyncio.sleep(10)

        expected_result = 0
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} order by timestamp desc")
        assert  float(result.result_rows[0][2]) == expected_result

    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")

