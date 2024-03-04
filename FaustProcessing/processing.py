import faust

from HealthStateModel.HealthCalculator import HealthCalculator
from HealthStateModel.HealthCalculatorThread import HealthCalculatorThread
from HealthStateModel.Writers.CompositeWriter import CompositeWriter
from ProcessingAdapter.FaustMeasurement import FaustMeasurement
from ProcessingAdapter.HealthModelProcessorAdapter import HealthModelProcessorAdapter

healthWriter = CompositeWriter().add_kafkaConfluent_writer("HealthScore", "kafka", "9092").add_stdOut_writer()
healthCalculator = HealthCalculator()
healthThread  = HealthCalculatorThread(healthCalculator,healthWriter,5)

temperature_topic = "temperature"
humidity_topic = "umidity"

app = faust.App('myapp', broker='kafka://kafka:9092')
topic = app.topic(temperature_topic,humidity_topic, value_type=FaustMeasurement)

measurement_processor = HealthModelProcessorAdapter(healthCalculator)

@app.agent(topic)
async def process(measurements):
    async for measurement in measurements:
        await measurement_processor.process_measurement(measurement)

healthThread.start()
app.main()
