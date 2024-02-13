import os

from Model.SimulatorExecutorAggregator import SimulatorExecutorAggregator
#from Model.Writers.KafkaWriter import KafkaWriter
from Model.Writers.StdoutWriter import StdoutWriter


KAFKA_HOST = os.environ.get("KAFKA_HOST", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

# Uso generale di una interfaccia Writer al fine di poter implementare quante politiche diverse di writing si vuole,
# senza dover cambiare nulla sul resto del codice.
# writeToStd = StdoutWriter()
writeToKafkaTemp = StdoutWriter() #KafkaWriter("temperature", KAFKA_HOST, KAFKA_PORT)
#writeToKafkaRain = KafkaWriter("rain", KAFKA_HOST, KAFKA_PORT)

symExecAggregator = SimulatorExecutorAggregator()

symExec = (
    symExecAggregator
    #.add_temperature_simulator(writeToKafkaTemp, 45.398214, 11.851271, 5)
    #.add_humidity_simulator(writeToKafkaTemp, 45.39214, 11.85271, 5)
    #.add_chargingStation_simulator(writeToKafkaTemp, 45.39214, 11.859271, 5)
    #.add_ecologicalIsland_simulator(writeToKafkaTemp, 45.391214, 11.8201271, 1)
    .add_waterPresence_simulator(writeToKafkaTemp, 45.391214, 11.8201271, 1)

    .get_simulator_executor()
)

symExec.run_all()
