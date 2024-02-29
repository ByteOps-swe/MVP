import pytest
import os
from Model.Simulators.Misurazione import Misurazione
from Model.Writers.KafkaWriter import KafkaWriter
from Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
import clickhouse_connect
KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

test_topic = "test_topic"


@pytest.mark.asyncio
async def test_1_misurazione():
    try:
        # Initialize ClickHouse client
        client = clickhouse_connect.get_client(host='clickhouse', port=8123, database ="innovacity")
        result = client.query('SELECT * FROM innovacity.temperatures where value =17 LIMIT 1')
        print(result.result_rows[0][3])
        assert float(result.result_rows[0][3]) == 17
    except Exception as e:
        pytest.fail(f"Failed to connect to ClickHouse database: {e}")
        #manca il finally close connection
