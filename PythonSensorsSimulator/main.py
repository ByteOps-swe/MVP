import os

from Model.SimulatorExecutorAggregator import SimulatorExecutorAggregator
from Model.Writers.KafkaWriter import KafkaWriter
from Model.Writers.StdoutWriter import StdoutWriter
from Model.Writers.kafkaAdapter.KafkaConfluentAdapter import KafkaConfluentAdapter

KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

# Uso generale di una interfaccia Writer al fine di poter implementare quante politiche diverse di writing si vuole,
# senza dover cambiare nulla sul resto del codice.
writeToStd = StdoutWriter()
writeToKafkaTemp =KafkaWriter(KafkaConfluentAdapter("temperature", KAFKA_HOST, KAFKA_PORT))
writeToKafkaUmd =KafkaWriter(KafkaConfluentAdapter("umidity", KAFKA_HOST, KAFKA_PORT))
writeToKafkaChargingStation =KafkaWriter(KafkaConfluentAdapter("chargingStation", KAFKA_HOST, KAFKA_PORT))
writeToKafkaEcologicalIsland =KafkaWriter(KafkaConfluentAdapter("ecologicalIsland", KAFKA_HOST, KAFKA_PORT))
writeToKafkaWaterPresence =KafkaWriter(KafkaConfluentAdapter("waterPresence", KAFKA_HOST, KAFKA_PORT))


symExecAggregator = SimulatorExecutorAggregator()
#MAYBE DECORATOR
symExec = (
    symExecAggregator
    .add_temperature_simulator([writeToKafkaTemp], 45.398214, 11.851271,"Arcella", 0.01)
    .add_temperature_simulator([writeToKafkaTemp], 45.388214, 11.691271,"Murelle", 0.01)
    .add_temperature_simulator([writeToKafkaTemp], 45.348214, 11.751271,"Montegrotto", 0.01)
    .add_temperature_simulator([writeToKafkaTemp], 45.368214, 11.951271,"Montegrotto", 0.01)

    .add_humidity_simulator([writeToKafkaUmd], 45.301214, 9.85271,"Arcella", 1)
    .add_humidity_simulator([writeToKafkaUmd], 45.201214, 9.85271,"Montegrotto", 1)

    .add_chargingStation_simulator([writeToKafkaChargingStation], 45.39214, 11.859271,"Arcella", 20)
    .add_chargingStation_simulator([writeToKafkaChargingStation], 45.79214, 11.959271,"Montegrotto", 20)

    .add_ecologicalIsland_simulator([writeToKafkaEcologicalIsland], 45.331214, 11.8901271,"Montegrotto", 4)
    .add_ecologicalIsland_simulator([writeToKafkaEcologicalIsland], 45.291214, 11.901271,"Murelle", 4)

    .add_waterPresence_simulator([writeToKafkaWaterPresence], 45.591214, 11.879001271,"Murelle", 1)

    .get_simulator_executor()
)

symExec.run_all()
