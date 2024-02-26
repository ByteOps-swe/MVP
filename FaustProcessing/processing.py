import faust

from HealthStateModel.HealthCalculator import HealthCalculator
from HealthStateModel.HealthCalculatorThread import HealthCalculatorThread
from HealthStateModel.Writers.CompositeWriter import CompositeWriter

healthWriter = CompositeWriter().add_kafkaConfluent_writer("HealthScore", "kafka", "9092")
healthCalculator = HealthCalculator(healthWriter)
healthThread  = HealthCalculatorThread(healthCalculator)

temperature_topic = "temperature"

class Measurement(faust.Record):
    timestamp: str
    value: float
    type: str
    latitude: float
    longitude: float
    ID_sensore: str
    cella: str

app = faust.App('myapp', broker='kafka://kafka:9092')
#app.topic(temperature_topic, humidity_topic, value_type=Measurement)
topic = app.topic(temperature_topic, value_type=Measurement)

# Definizione dell'agente Faust
@app.agent(topic)
async def process(measurements):
    async for measurement in measurements:
        healthCalculator.add_misurazione(measurement.timestamp, measurement.value, measurement.type, measurement.latitude, measurement.longitude, measurement.ID_sensore, measurement.cella)

app.main()
healthThread.run()
