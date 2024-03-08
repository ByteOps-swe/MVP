from HealthStateModel.HealthCalculator import HealthCalculator
from .FaustMeasurement import FaustMeasurement
from .FaustProcessor import Processor
class HealthModelProcessorAdapter(Processor):
    """
    Adapter class for processing health model measurements.
    """

    def __init__(self, healthCalculator:HealthCalculator):
        self.healthCalculator = healthCalculator

    async def process_measurement(self, measurement:FaustMeasurement):
        """
        Process a measurement and add it to the health calculator.

        Args:
            measurement (FaustMeasurement): The measurement to be processed.
        """
        self.healthCalculator.add_misurazione(measurement.timestamp, measurement.value, measurement.type, measurement.latitude, measurement.longitude, measurement.ID_sensore, measurement.cella)
