import pytest
import os
import asyncio
import faust
import warnings

from Model.Simulators.Misurazione import Misurazione
from Model.Writers.KafkaWriter import KafkaWriter
from Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

test_topic = "test_topic"

@pytest.mark.asyncio
async def test_1_misurazione():
    warnings.filterwarnings("ignore")

    adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
    kafka_writer = KafkaWriter(adapter_kafka)
    misurazione = Misurazione('2024-02-28 10:20:37.206573', 17, "Temperature", 45.39214, 11.859271, "Tmp1", "Arcella")
    kafka_writer.write(misurazione) 
    app = faust.App('myapp', broker=f'kafka://{KAFKA_HOST}:{KAFKA_PORT}')
    topic = app.topic(test_topic, value_type=str) 

    measurement_list = []
    @app.agent(topic)
    async def process(measurements):
        async for measurement in measurements:
            measurement_list.append(measurement)
            # Controlla l'assert non appena viene ricevuto il messaggio
            assert misurazione.to_json() == measurement
            break  # Esci dal loop dopo aver ricevuto il messaggio

    await app.start()
    await app.stop()

@pytest.mark.asyncio
async def test_100_misurazioni():
    warnings.filterwarnings("ignore")

    adapter_kafka = KafkaConfluentAdapter(test_topic, KAFKA_HOST, KAFKA_PORT)
    kafka_writer = KafkaWriter(adapter_kafka)
    app = faust.App('myapp', broker=f'kafka://{KAFKA_HOST}:{KAFKA_PORT}')
    topic = app.topic(test_topic, value_type=str) 
    sent_measurements = []  # Lista delle misurazioni inviate
    expected_measurements = 100
    for i in range(expected_measurements):
        misurazione = Misurazione(f'2024-02-28 10:20:37.{i:03}', i, "Temperature", 45.39214 + i, 11.859271 + i, "Tmp1", "Arcella")
        kafka_writer.write(misurazione)
        sent_measurements.append(misurazione.to_json())  # Aggiungi la misurazione inviata alla lista
   

    @app.agent(topic)
    async def process(measurements):
        nonlocal sent_measurements
        async for measurement in measurements:
            # Controlla che la misurazione ricevuta sia presente nella lista delle misurazioni inviate
            assert measurement in sent_measurements
            sent_measurements.remove(measurement)  # Rimuovi la misurazione dalla lista delle inviate
            if not sent_measurements:  # Se tutte le misurazioni sono state ricevute, interrompi il loop
                break

    await app.start()
    await app.stop()

