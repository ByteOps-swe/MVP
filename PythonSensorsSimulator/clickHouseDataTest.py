import pytest
import os
from Model.Simulators.Misurazione import Misurazione
from Model.Writers.KafkaWriter import KafkaWriter
from Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter
from Test.ClickHouseClient import ClickHouseClient

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

test_topic = "test_topic"


@pytest.mark.asyncio
async def test_1_misurazione():
    # Initialize ClickHouse client
    clickhouse_client = ClickHouseClient("clickhouse", "8123", user="", password="", database="innovacity")
    clickhouse_client.connect()

    # Write test data to ClickHouse
    misurazione = Misurazione('2024-02-28 10:20:37.206573', 17, "Temperature", 45.39214, 11.859271, "Tmp1", "Arcella")
    clickhouse_client.execute_query(f"INSERT INTO your_table VALUES {misurazione.to_tuple()}")

    # Retrieve inserted data from ClickHouse
    select_query = f"SELECT * FROM your_table WHERE timestamp = '2024-02-28 10:20:37.206573'"  # Adjust the query according to your table schema
    result = clickhouse_client.execute_query(select_query)

    # Verify that the data received from ClickHouse matches the data sent
    assert result == [misurazione.to_tuple()]

    # Close ClickHouse connection
    clickhouse_client.close()
