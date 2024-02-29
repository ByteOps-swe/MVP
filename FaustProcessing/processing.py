import faust

from HealthStateModel.HealthCalculator import HealthCalculator
from HealthStateModel.HealthCalculatorThread import HealthCalculatorThread
from HealthStateModel.Writers.CompositeWriter import CompositeWriter

healthWriter = CompositeWriter().add_kafkaConfluent_writer("HealthScore", "kafka", "9092").add_stdOut_writer()
healthCalculator = HealthCalculator()
healthThread  = HealthCalculatorThread(healthCalculator,healthWriter,5)

temperature_topic = "temperature"
humidity_topic = "umidity"
class Measurement(faust.Record):
    timestamp: str
    value: float
    type: str
    latitude: float
    longitude: float
    ID_sensore: str
    cella: str

app = faust.App('myapp', broker='kafka://kafka:9092')
topic = app.topic(temperature_topic,humidity_topic, value_type=Measurement)

@app.agent(topic)
async def process(measurements):
    async for measurement in measurements:
        healthCalculator.add_misurazione(measurement.timestamp, measurement.value, measurement.type, measurement.latitude, measurement.longitude, measurement.ID_sensore, measurement.cella)

healthThread.start()
app.main()

