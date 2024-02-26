import faust
import asyncio

from HealthStateModel.HealthCalculator import HealthCalculator
from HealthStateModel.Writers.CompositeWriter import CompositeWriter
import os


KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")
# Uso generale di una interfaccia Writer al fine di poter implementare quante politiche diverse di writing si vuole,
# senza dover cambiare nulla sul resto del codice.

healthWriter = CompositeWriter().add_kafkaConfluent_writer("HealthScore", KAFKA_HOST, KAFKA_PORT)
healthCalculator = HealthCalculator(healthWriter)

class Measurement(faust.Record):
    timestamp: str
    value: float
    type: str
    latitude: float
    longitude: float
    ID_sensore: str
    cella: str

app = faust.App('myapp', broker='kafka://kafka:9092')
topic = app.topic(HealthCalculator.temperature_topic, value_type=Measurement)

# Definizione dell'agente Faust
@app.agent(topic)
async def process(measurements):
    async for measurement in measurements:
        healthCalculator.add_misurazione(measurement.timestamp, measurement.value, HealthCalculator.temperature_topic, measurement.latitude, measurement.longitude, measurement.ID_sensore, measurement.cella)
        healthCalculator.generate_new_health_score()

if __name__ == '__main__':
    app.main()
    