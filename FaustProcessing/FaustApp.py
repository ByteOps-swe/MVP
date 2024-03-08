import faust
from ProcessingAdapter.FaustMeasurement import FaustMeasurement
from ProcessingAdapter.FaustProcessor import Processor


def getFaustApp(broker, processor:Processor, tmp_topic, umd_topic, dustPm10_topic):
    app = faust.App('myapp', broker=broker)
    topic = app.topic(tmp_topic, umd_topic, dustPm10_topic, value_type=FaustMeasurement)

    @app.agent(topic)
    async def process(measurements):
        try:
            async for measurement in measurements:
                await processor.process_measurement(measurement)
        except Exception as e:
            print(f"Errore durante il processamento delle misurazioni: {e}")

        return app.main()