import os

from Model.Simulators.SensorFactory import SensorFactory

from Model.SimulatorExecutorFactory import SimulatorExecutorFactory
from Model.Writers.CompositeWriter import CompositeWriter

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")
# Uso generale di una interfaccia Writer al fine di poter implementare quante politiche diverse di writing si vuole,
# senza dover cambiare nulla sul resto del codice.

temp_writers = CompositeWriter().add_kafkaConfluent_writer("temperature", KAFKA_HOST, KAFKA_PORT)
umd_writers = CompositeWriter().add_kafkaConfluent_writer("umidity", KAFKA_HOST, KAFKA_PORT)
chS_writers = CompositeWriter().add_kafkaConfluent_writer("chargingStation", KAFKA_HOST, KAFKA_PORT)
ecoIs_writers = CompositeWriter().add_kafkaConfluent_writer("ecologicalIsland", KAFKA_HOST, KAFKA_PORT)
waPr_writers = CompositeWriter().add_kafkaConfluent_writer("waterPresence", KAFKA_HOST, KAFKA_PORT)
dust_writers = CompositeWriter().add_kafkaConfluent_writer("dust_level_PM10", KAFKA_HOST, KAFKA_PORT)
eletricalFault_writers = CompositeWriter().add_kafkaConfluent_writer("electrical_fault", KAFKA_HOST, KAFKA_PORT)

"""
from Model.Writers.StdoutWriter import StdoutWriter
stdout = StdoutWriter()
"""
symExecAggregator = SimulatorExecutorFactory()

symExecAggregator \
    .add_simulator(SensorFactory.create_humidity_sensor(umd_writers, 45.301214, 11.789271, "Arcella", 2)) \
    .add_simulator(SensorFactory.create_humidity_sensor(umd_writers, 45.291214, 11.787271, "Montegrotto", 2)) \
    .add_simulator(SensorFactory.create_charging_station_sensor(chS_writers, 45.39214, 11.859271, "Arcella", 1)) \
    .add_simulator(SensorFactory.create_charging_station_sensor(chS_writers, 45.40214, 11.959271, "Montegrotto", 2)) \
    .add_simulator(SensorFactory.create_ecological_island_sensor(ecoIs_writers, 45.331214, 11.8901271, "Montegrotto", 2)) \
    .add_simulator(SensorFactory.create_ecological_island_sensor(ecoIs_writers, 45.291214, 11.901271, "Murelle", 1))  \
    .add_simulator(SensorFactory.create_dust_PM10_sensor(dust_writers, 45.272214, 11.931271, "Murelle", 1))  \
    .add_simulator(SensorFactory.create_dust_PM10_sensor(dust_writers, 45.282314, 11.921271, "Montegrotto", 1))  \
    .add_simulator(SensorFactory.create_eletrical_fault_sensor(eletricalFault_writers, 45.268214, 11.931271, "Murelle", 10))  \
    .add_simulator(SensorFactory.create_eletrical_fault_sensor(eletricalFault_writers, 45.279114, 11.891271, "Montegrotto", 10))  \
.add_simulator(SensorFactory.create_water_presence_sensor(waPr_writers, 45.591214, 11.879001271,"Murelle", 2)) \
.run()

