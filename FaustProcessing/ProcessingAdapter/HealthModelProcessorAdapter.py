from HealthStateModel.HealthProcessorBuffer import HealthProcessorBuffer
from .FaustMeasurement import FaustMeasurement
from .FaustProcessor import Processor

class HealthModelProcessorAdapter(Processor):
    def __init__(self, healthCalculator:HealthProcessorBuffer):
        self.healthCalculator = healthCalculator

    async def process(self, misurazione:FaustMeasurement):
        self.healthCalculator.add_misurazione(misurazione.timestamp,
                                                misurazione.value,
                                                misurazione.type,
                                                misurazione.latitude,
                                                misurazione.longitude,
                                                misurazione.ID_sensore,
                                                misurazione.cella)
