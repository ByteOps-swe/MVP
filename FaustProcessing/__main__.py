import faust

from .HealthStateModel.HealthCalculator import HealthCalculator
from .HealthStateModel.HealthCalculatorThread import HealthCalculatorThread
from .HealthStateModel.Writers.CompositeWriter import CompositeWriter
from .ProcessingAdapter.FaustMeasurement import FaustMeasurement
from .ProcessingAdapter.HealthModelProcessorAdapter import HealthModelProcessorAdapter
from FaustApp import getFaustApp

healthWriter = CompositeWriter().add_kafkaConfluent_writer("HealthScore", "kafka", "9092").add_stdOut_writer()
healthCalculator = HealthCalculator()
healthThread  = HealthCalculatorThread(healthCalculator,healthWriter,5)
appF = getFaustApp('kafka://kafka:9092', healthCalculator, "temperature", "umidity", "dust_level_PM10")


# app = faust.App('myapp', broker='kafka://kafka:9092')
# topic = app.topic(temperature_topic,humidity_topic,dustPm10_topic, value_type=FaustMeasurement)

# measurement_processor = HealthModelProcessorAdapter(healthCalculator)

# @app.agent(topic)
# async def process(measurements):
#     try:
#         async for measurement in measurements:
#             await measurement_processor.process_measurement(measurement)
#     except Exception as e:
#         print(f"Errore durante il processamento delle misurazioni: {e}")

# @app.task()
# async def mytask():
#     healthThread.start()

# appF.main()