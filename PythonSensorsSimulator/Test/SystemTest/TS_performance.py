# pylint: skip-file
import os
from datetime import datetime,timedelta
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

@pytest.fixture(scope='module')
def kafka_write():
    adapter_kafka = kafka_confluent_adapter(test_topic, KAFKA_HOST, KAFKA_PORT)
    kafka_write = kafka_writer(adapter_kafka)
    yield kafka_write


@pytest.mark.asyncio
async def test_1_misurazione_time_pipeline(clickhouse_client, kafka_write):
    try:
        timestamp = datetime.now()
        measure = adapter_misurazione(
                        misurazione(timestamp, 0, "Temperature", coordinate(45.39214, 11.859271), "id_t_perf_1", "T_perf_cell"))
        kafka_write.write(measure)
        kafka_write.flush_kafka_producer()
        
        query = f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='id_t_perf_1' and timestamp = '{timestamp}' LIMIT 1"

        query_time_before = datetime.now()
        result = clickhouse_client.query(query)
        query_time_after = datetime.now()
        iter = 0
        max_seconds_to_wait = 10
        intervallo_sleep = 0.5
        while (not result.result_rows) and (iter * intervallo_sleep < max_seconds_to_wait):
            await asyncio.sleep(intervallo_sleep)
            query_time_before = datetime.now()
            result = clickhouse_client.query(query)
            query_time_after = datetime.now()
            iter += 1

        assert result.result_rows
        time_difference = abs(result.result_rows[0][6] - timestamp)
        # print(f"Message sended at:{timestamp} \n \t and arrived at:{result.result_rows[0][6]},\n\t la differenza è di: {time_difference} \n\tSelect query time: {query_time_after - query_time_before} \n")
        assert time_difference < timedelta(seconds=10)

    except Exception as e:
        pytest.fail(f"Failed to send and consume data: {e}")

@pytest.mark.asyncio
async def test_multi_misurazione_time_pipeline(clickhouse_client, kafka_write):
    try:
        num_messages = 1000
        starting_value = 0
        timestamps = []
        for i in range(num_messages):
            timestamps.append(datetime.now())
            measure = adapter_misurazione(
                            misurazione(timestamps[i], starting_value + i, "Temperature", coordinate(45.39214, 11.859271), "id_t_perf_multi", "T_perf_cell"))
            kafka_write.write(measure)
        kafka_write.flush_kafka_producer()
        time_sent = datetime.now()
        query = f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='id_t_perf_multi' and timestamp >= '{timestamps[0]}' ORDER BY (timestamp,value)   DESC LIMIT {num_messages}"
        result = clickhouse_client.query(query)
        iter = 0
        max_seconds_to_wait = 10
        intervallo_sleep = 0.5
        while (len(result.result_rows) < num_messages) and (iter * intervallo_sleep < max_seconds_to_wait):
            await asyncio.sleep(intervallo_sleep)
            result = clickhouse_client.query(query)
            iter += 1

        for i in range(num_messages):
            time_difference = abs(result.result_rows[i][6] - time_sent)
            # print(f"Message sent at:{time_sent}\n\t and arrived at:{result.result_rows[i][6]},\n\t la differenza è di: {time_difference} secondi\n")
            assert time_difference < timedelta(seconds=10)
    except Exception as e:
        pytest.fail(f"Failed to send and consume data: {e}")