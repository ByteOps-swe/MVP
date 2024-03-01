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
        # client = clickhouse_connect.get_client(host='clickhouse', port=8123, database ="innovacity")
        # result = client.query('SELECT * FROM innovacity.temperatures where value =17 LIMIT 1')
        # print(result.result_rows[0][3])
        adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
        kafka_writer = KafkaWriter(adapter_kafka)
        misurazione = AdapterMisurazione(Misurazione('2022-02-28 10:20:37.206573', 4001, "Temperature", Coordinate(45.39214, 11.859271), "Tmp1", "Arcella1"))
        kafka_writer.write(misurazione) 
        kafka_writer.flush_kafka_producer()
        time.sleep(10)
        result = clickhouse_client.query('SELECT * FROM innovacity.temperatures where value =4001 LIMIT 1')
        print(result.result_rows)
        assert result.result_rows
        assert float(result.result_rows[0][3]) == 4001
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")
