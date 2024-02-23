import os
import threading
import time

from Model.SimulatorExecutorFactory import SimulatorExecutorFactory
from Model.Writers.KafkaWriter import KafkaWriter
from Model.Writers.StdoutWriter import StdoutWriter
from Model.Writers.ListWriter import ListWriter

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
#TEST WRITER
# Creazione degli oggetti ListWriter
list_writers = {
    "list_writer_tmp": ListWriter(),
    "list_writer_umd": ListWriter(),
    "list_writer_chSt": ListWriter(),
    "list_writer_ecoIs": ListWriter(),
    "list_writer_waterPr": ListWriter()
}



symExecAggregator = SimulatorExecutorFactory()
#MAYBE DECORATOR
symExec = (
    symExecAggregator
    .add_temperature_simulator([writeToKafkaTemp,list_writers["list_writer_tmp"]], 45.398214, 11.851271,"Arcella", 0.5)
    .add_temperature_simulator([writeToKafkaTemp,list_writers["list_writer_tmp"]], 45.388214, 11.691271,"Murelle", 0.5)
    .add_temperature_simulator([writeToKafkaTemp,list_writers["list_writer_tmp"]], 45.348214, 11.751271,"Montegrotto", 0.5)
    .add_temperature_simulator([writeToKafkaTemp,list_writers["list_writer_tmp"]], 45.368214, 11.951271,"Montegrotto", 0.5)

    .add_humidity_simulator([writeToKafkaUmd,list_writers["list_writer_umd"]], 45.301214, 9.85271,"Arcella", 1)
    .add_humidity_simulator([writeToKafkaUmd,list_writers["list_writer_umd"]], 45.201214, 9.85271,"Montegrotto", 1)

    .add_chargingStation_simulator([writeToKafkaChargingStation,list_writers["list_writer_chSt"]], 45.39214, 11.859271,"Arcella", 20)
    .add_chargingStation_simulator([writeToKafkaChargingStation,list_writers["list_writer_chSt"]], 45.79214, 11.959271,"Montegrotto", 20)

    .add_ecologicalIsland_simulator([writeToKafkaEcologicalIsland,list_writers["list_writer_ecoIs"]], 45.331214, 11.8901271,"Montegrotto", 4)
    .add_ecologicalIsland_simulator([writeToKafkaEcologicalIsland,list_writers["list_writer_ecoIs"]], 45.291214, 11.901271,"Murelle", 4)

    .add_waterPresence_simulator([writeToKafkaWaterPresence,list_writers["list_writer_waterPr"]], 45.591214, 11.879001271,"Murelle", 1)

    .get_simulator_executor()
)

symExec.run_all()



# Funzione per chiamare il metodo get_data_list per ogni oggetto ListWriter dopo 30 secondi
def call_get_data_list_after_delay(writers_list, database,queries ):
    time.sleep(30)  # Attende 30 secondi
    symExec.stop_all()
    i = 0
    for list_writer_name, list_writer_object in list_writers.items():
        data_list = list_writer_object.get_data_list()
        results = client.execute_query(queries[i])
        i = i+1
        for row in results:
            print(row)




from Test.ClickHouseClient import ClickHouseClient
# Definisci i valori per le variabili
host = "clickhouse"
port = 9000
user = ""  # Lascialo vuoto se non ci sono credenziali
password = ""  # Lascialo vuoto se non ci sono credenziali
database = "innovacity"  # Database specificato come CLICKHOUSE_DB

# Crea un'istanza della classe ClickHouseClient
client = ClickHouseClient(host=host, port=port, user=user, password=password, database=database)
client.connect()

queries = ['SELECT * FROM innovacity.temperatures_kafka',
'SELECT * FROM innovacity.temperatures_kafka',
'SELECT * FROM innovacity.chargingStation_kafka',
'SELECT * FROM innovacity.ecoIslands_kafka',
'SELECT * FROM innovacity.waterPresence_kafka',
]




# Chiamata della funzione per chiamare il metodo get_data_list dopo 30 secondi per ogni oggetto ListWriter
call_get_data_list_after_delay(list_writers, client, queries)


client.close()