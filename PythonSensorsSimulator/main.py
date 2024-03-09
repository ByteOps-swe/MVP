import os

from .Model.Simulators.SensorFactory import SensorFactory
from .Model.SimulatorExecutorFactory import SimulatorExecutorFactory
from .Model.Writers.CompositeWriter import CompositeWriter

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")
# Uso generale di una interfaccia Writer al fine di poter implementare quante politiche diverse di writing si vuole,
# senza dover cambiare nulla sul resto del codice.

temp_writers = CompositeWriter().add_kafkaConfluent_writer("temperature", KAFKA_HOST, KAFKA_PORT)
umd_writers = CompositeWriter().add_kafkaConfluent_writer("humidity", KAFKA_HOST, KAFKA_PORT)
chS_writers = CompositeWriter().add_kafkaConfluent_writer("chargingStation", KAFKA_HOST, KAFKA_PORT)
ecoIs_writers = CompositeWriter().add_kafkaConfluent_writer("ecologicalIsland", KAFKA_HOST, KAFKA_PORT)
waPr_writers = CompositeWriter().add_kafkaConfluent_writer("waterPresence", KAFKA_HOST, KAFKA_PORT)
dust_writers = CompositeWriter().add_kafkaConfluent_writer("dust_PM10", KAFKA_HOST, KAFKA_PORT)
eletricalFault_writers = CompositeWriter().add_kafkaConfluent_writer("electrical_fault", KAFKA_HOST, KAFKA_PORT)
symExecAggregator = SimulatorExecutorFactory()

symExecAggregator \
    .add_simulator(SensorFactory.create_temperature_sensor(45.4065, 11.8793, "Centro storico"), temp_writers, 1) \
    .add_simulator(SensorFactory.create_temperature_sensor(45.396661, 11.898114, "Terranegra"), temp_writers, 1) \
    .add_simulator(SensorFactory.create_temperature_sensor(45.398438, 11.861783, "Sacra Famiglia"), temp_writers, 1) \
    .add_simulator(SensorFactory.create_humidity_sensor(45.4068, 11.8794, "Centro storico"), umd_writers, 1) \
    .add_simulator(SensorFactory.create_humidity_sensor(45.398319, 11.903093, "Terranegra"), umd_writers, 1) \
    .add_simulator(SensorFactory.create_humidity_sensor(45.396324, 11.863110, "Sacra Famiglia"), umd_writers, 1) \
    .add_simulator(SensorFactory.create_charging_station_sensor(45.4059, 11.8785, "Centro storico"), chS_writers, 1) \
    .add_simulator(SensorFactory.create_charging_station_sensor(45.399434, 11.905925, "Terranegra"), chS_writers, 1) \
    .add_simulator(SensorFactory.create_charging_station_sensor(45.398259, 11.864335, "Sacra Famiglia"), chS_writers, 1) \
    .add_simulator(SensorFactory.create_ecological_island_sensor(45.4045, 11.8797, "Centro storico"), ecoIs_writers, 1) \
    .add_simulator(SensorFactory.create_ecological_island_sensor(45.394024, 11.899316, "Terranegra"), ecoIs_writers, 1) \
    .add_simulator(SensorFactory.create_ecological_island_sensor(45.395392, 11.862549, "Sacra Famiglia"), ecoIs_writers, 1) \
    .add_simulator(SensorFactory.create_dust_PM10_sensor(45.4069, 11.8800, "Centro storico"), dust_writers, 1) \
    .add_simulator(SensorFactory.create_dust_PM10_sensor(45.397430, 11.907513, "Terranegra"), dust_writers, 1) \
    .add_simulator(SensorFactory.create_dust_PM10_sensor(45.395679, 11.864794, "Sacra Famiglia"), dust_writers, 1) \
    .add_simulator(SensorFactory.create_eletrical_fault_sensor(45.4056, 11.8788, "Centro storico"), eletricalFault_writers, 1) \
    .add_simulator(SensorFactory.create_eletrical_fault_sensor(45.393181, 11.907685, "Terranegra"), eletricalFault_writers, 1) \
    .add_simulator(SensorFactory.create_eletrical_fault_sensor(45.395320, 11.859793, "Sacra Famiglia"), eletricalFault_writers, 1) \
    .add_simulator(SensorFactory.create_water_presence_sensor(45.4070, 11.8805, "Centro storico"), waPr_writers, 1) \
    .add_simulator(SensorFactory.create_water_presence_sensor(45.393142, 11.895443, "Terranegra"), waPr_writers, 1) \
    .add_simulator(SensorFactory.create_water_presence_sensor(45.398187, 11.865407, "Sacra Famiglia"), waPr_writers, 1) \
    .run()
