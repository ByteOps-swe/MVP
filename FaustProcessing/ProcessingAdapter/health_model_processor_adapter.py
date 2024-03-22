from HealthStateModel.health_processor_buffer import health_processor_buffer
from .faust_measurement import faust_measurement
from .faust_processor import processor

class health_model_processor_adapter(processor):
    def __init__(self, health_calculator:health_processor_buffer):
        self.health_calculator = health_calculator

    async def process(self, misurazione:faust_measurement):
        self.health_calculator.add_misurazione(misurazione.timestamp,
                                                misurazione.value,
                                                misurazione.type,
                                                misurazione.latitude,
                                                misurazione.longitude,
                                                misurazione.ID_sensore,
                                                misurazione.cella)
