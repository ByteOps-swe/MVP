import pytest
import os
from .Model.Simulators.Coordinate import Coordinate
from .Model.Simulators.Misurazione import Misurazione
from .Model.Writers.KafkaWriter import KafkaWriter
from .Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
from .Model.AdapterMisurazione import AdapterMisurazione
import clickhouse_connect
import time
KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

test_topic = "temperature"


@pytest.fixture(scope='module')
def clickhouse_client():
    # Set up ClickHouse client
    client = clickhouse_connect.get_client(host='clickhouse', port=8123, database="innovacity")
    yield client
    # Teardown: Close connection after all tests in the module have run
    client.close()

@pytest.mark.asyncio
async def test_1_misurazione(clickhouse_client):
    try:
        adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
        kafka_writer = KafkaWriter(adapter_kafka)
        misurazione = AdapterMisurazione(Misurazione('2021-02-28 10:20:37.206573', 4001, "Temperature", Coordinate(45.39214, 11.859271), "Tmp1", "Arcella1"))
        kafka_writer.write(misurazione) 
        kafka_writer.flush_kafka_producer()
        time.sleep(1)
        result = clickhouse_client.query('SELECT * FROM innovacity.temperatures where value =4001 LIMIT 1')
        print(result.result_rows)
        assert result.result_rows
        assert float(result.result_rows[0][3]) == 4001
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")
        


@pytest.mark.asyncio
async def test_2_misurazione(clickhouse_client):
    try:
        adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
        kafka_writer = KafkaWriter(adapter_kafka)
        num_messages = 10  # Number of messages to send
        
        # Send data to Kafka
        for i in range(num_messages):
            misurazione = AdapterMisurazione(Misurazione(f'2020-02-28 10:20:37.1{i}', 5001 + i, "Temperature", Coordinate(45.39214, 11.859271), "Tmp1", "ArcellaTest"))
            kafka_writer.write(misurazione) 
        kafka_writer.flush_kafka_producer()
        time.sleep(10)
        
        # Query ClickHouse to check if all data has been inserted
        result = clickhouse_client.query(f"SELECT * FROM innovacity.temperatures WHERE cella = 'ArcellaTest'")
        print(result.result_rows)
        for i in range(num_messages):
            print(result.result_rows[i][2])
            assert float(result.result_rows[i][3]) == 5001 + i

    except Exception as e:
        pytest.fail(f"Failed to send and consume data: {e}")