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
test_topic = "test"
table_to_test = "test"

@pytest.fixture(scope='module')
def clickhouse_client():
    client = clickhouse_connect.get_client(host='clickhouse', port=8123, database="innovacity")
    yield client
    client.close()

@pytest.fixture(scope='module')
def kafka_writer():
    adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
    kafka_writer = KafkaWriter(adapter_kafka)
    yield kafka_writer


@pytest.mark.asyncio
async def test_multiple_misurazioni(clickhouse_client,kafka_writer):
    try:
        num_messages = 10000  # Number of messages to send
        starting_value = 0
        timestamps = []
        for i in range(num_messages):
            timestamp = datetime.now()
            timestamps.append(timestamp)
            misurazione = AdapterMisurazione(
                            Misurazione(timestamp, starting_value + i, "Temperature", Coordinate(45.39214, 11.859271), "id_t_carico", "T_carico_cell"))
            kafka_writer.write(misurazione)
        kafka_writer.flush_kafka_producer()
        
        await asyncio.sleep(10)

        # Query ClickHouse to check if all data has been inserted
        result = clickhouse_client.query(f"SELECT * FROM innovacity.{table_to_test} where ID_sensore ='id_t_carico' ORDER BY (timestamp,value) DESC LIMIT {num_messages}")
        print(len(result.result_rows))
        print(result.result_rows)
        for i in range(num_messages):
            assert (starting_value + num_messages - 1 -i) == float(result.result_rows[i][3])
            assert str(timestamps[num_messages -1 -i])[:19] == str(result.result_rows[i][2])[:19]
    except Exception as e:
        pytest.fail(f"Failed to send and consume data: {e}")
