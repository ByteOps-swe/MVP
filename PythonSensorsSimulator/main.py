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
"""
from Model.Writers.StdoutWriter import StdoutWriter
stdout = StdoutWriter()
"""
symExecAggregator = SimulatorExecutorFactory()
"""
symExecAggregator \
    .add_temperature_simulator(temp_writers, 45.398214, 11.851271, "Arcella", 0.5) \
    .add_temperature_simulator(temp_writers, 45.388214, 11.691271, "Murelle", 0.5) \
    .add_temperature_simulator(temp_writers, 45.348214, 11.751271, "Montegrotto", 0.5) \
    .add_temperature_simulator(temp_writers, 45.368214, 11.951271, "Montegrotto", 0.5) \
    .add_humidity_simulator(umd_writers, 45.301214, 11.789271, "Arcella", 1) \
    .add_humidity_simulator(umd_writers, 45.291214, 11.787271, "Montegrotto", 1) \
    .add_chargingStation_simulator(chS_writers, 45.39214, 11.859271, "Arcella", 20) \
    .add_chargingStation_simulator(chS_writers, 45.40214, 11.959271, "Montegrotto", 20) \
    .add_ecologicalIsland_simulator(ecoIs_writers, 45.331214, 11.8901271, "Montegrotto", 4) \
    .add_ecologicalIsland_simulator(ecoIs_writers, 45.291214, 11.901271, "Murelle", 4)  \
.add_waterPresence_simulator(waPr_writers, 45.591214, 11.879001271,"Murelle", 1) \
.run()"""

symExecAggregator \
    .add_simulator(SensorFactory.create_temperature_sensor(temp_writers, 45.398214, 11.851271, "Arcella", 1)) \
    .add_simulator(SensorFactory.create_temperature_sensor(temp_writers, 45.388214, 11.691271, "Murelle", 1)) \
    .add_simulator(SensorFactory.create_temperature_sensor(temp_writers, 45.348214, 11.751271, "Montegrotto", 1)) \
    .add_simulator(SensorFactory.create_temperature_sensor(temp_writers, 45.368214, 11.951271, "Montegrotto", 1)) \
    .add_simulator(SensorFactory.create_humidity_sensor(umd_writers, 45.301214, 11.789271, "Arcella", 2)) \
    .add_simulator(SensorFactory.create_humidity_sensor(umd_writers, 45.291214, 11.787271, "Montegrotto", 2)) \
    .add_simulator(SensorFactory.create_charging_station_sensor(chS_writers, 45.39214, 11.859271, "Arcella", 1)) \
    .add_simulator(SensorFactory.create_charging_station_sensor(chS_writers, 45.40214, 11.959271, "Montegrotto", 2)) \
    .add_simulator(SensorFactory.create_ecological_island_sensor(ecoIs_writers, 45.331214, 11.8901271, "Montegrotto", 2)) \
    .add_simulator(SensorFactory.create_ecological_island_sensor(ecoIs_writers, 45.291214, 11.901271, "Murelle", 1))  \
.add_simulator(SensorFactory.create_water_presence_sensor(waPr_writers, 45.591214, 11.879001271,"Murelle", 2)) \
.run()

