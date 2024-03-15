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
    adapter_kafka = kafka_confluent_adapter(test_topic, KAFKA_HOST, KAFKA_PORT)
    kafka_writer = kafka_writer(adapter_kafka)
    yield kafka_writer

@pytest.mark.asyncio
async def test_1_misurazione(clickhouse_client,kafka_writer):
    try:
        timestamp = datetime.now()
        misurazione = adapter_misurazione(
            misurazione(timestamp, 4001, "Temperature", coordinate(45.39214, 11.859271), "Id_1_mis_test", "Arcella1"))
        kafka_writer.write(misurazione)
        kafka_writer.flush_kafka_producer()

        query = f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='Id_1_mis_test' and timestamp = '{str(timestamp)}' LIMIT 1"

        result = clickhouse_client.query(query)
        iter = 0
        max_seconds_to_wait = 7
        intervallo_sleep = 0.5
        while (not result.result_rows) and (iter * intervallo_sleep < max_seconds_to_wait):
            await asyncio.sleep(intervallo_sleep)
            result = clickhouse_client.query(query)
            iter += 1
        
        #print(result.result_rows)
        assert result.result_rows
        assert float(result.result_rows[0][3]) == 4001
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")

@pytest.mark.asyncio
async def test_multiple_misurazioni(clickhouse_client,kafka_writer):
    try:
        num_messages = 100  # Number of messages to send
        starting_value = 5001
        timestamps = []
        for i in range(num_messages):
            timestamp = datetime.now()
            timestamps.append(timestamp)
            misurazione = adapter_misurazione(
                            misurazione(timestamp, starting_value + i, "Temperature", coordinate(45.39214, 11.859271), "Id_multi_mis_test", "ArcellaTest"))
            kafka_writer.write(misurazione)
        kafka_writer.flush_kafka_producer()
       
       
        query = f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='Id_multi_mis_test'  and timestamp >= '{timestamps[0]}' ORDER BY (timestamp,value) DESC LIMIT {num_messages}"
        result = clickhouse_client.query(query)
        iter = 0
        max_seconds_to_wait = 10
        intervallo_sleep = 0.5
        while (len(result.result_rows) < num_messages) and (iter * intervallo_sleep < max_seconds_to_wait):
            await asyncio.sleep(intervallo_sleep)
            result = clickhouse_client.query(query)
            iter += 1

       # print(result.result_rows)
        for i in range(num_messages):
            assert (starting_value + num_messages - 1 -i) == float(result.result_rows[i][3])
            assert timestamps[num_messages -1 -i] == result.result_rows[i][2]
    except Exception as e:
        pytest.fail(f"Failed to send and consume data: {e}")
