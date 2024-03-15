import faust

from HealthStateModel.health_calculator import health_calculator
from HealthStateModel.health_calculator_thread import health_calculator_thread
from HealthStateModel.Writers.composite_writer import composite_writer
from ProcessingAdapter.faust_measurement import faust_measurement
from ProcessingAdapter.health_model_processor_adapter import health_model_processor_adapter

healthWriter = composite_writer().add_kafka_confluent_writer("HealthScore", "kafka", "9092").add_std_out_writer()
health_calculator = health_calculator()
healthThread  = health_calculator_thread(health_calculator,healthWriter,5)

temperature_topic = "temperature"
humidity_topic = "humidity"
dustPm10_topic = "dust_PM10"


app = faust.App('myapp', broker='kafka://kafka:9092')
topic = app.topic(temperature_topic,humidity_topic,dustPm10_topic, value_type=faust_measurement)

measurement_processor = health_model_processor_adapter(health_calculator)

@app.agent(topic)
async def process(measurements):
    try:
        async for measurement in measurements:
            await measurement_processor.process(measurement)
    except Exception as e:
        print(f"Errore durante il processamento delle misurazioni: {e}")

@app.task()
async def mytask():
    healthThread.start()

app.main()
