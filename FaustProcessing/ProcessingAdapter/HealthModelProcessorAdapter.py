from HealthStateModel.HealthCalculator import HealthCalculator
from .FaustMeasurement import FaustMeasurement
from .FaustProcessor import Processor
class HealthModelProcessorAdapter(Processor):
    def __init__(self, healthCalculator:HealthCalculator):
        self.healthCalculator = healthCalculator

    async def process_measurement(self, measurement:FaustMeasurement):
        self.healthCalculator.add_misurazione(measurement.timestamp,
                                                measurement.value,
                                                measurement.type,
                                                measurement.latitude,
                                                measurement.longitude,
                                                measurement.ID_sensore,
                                                measurement.cella)
