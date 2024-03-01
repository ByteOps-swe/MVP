# InnovaCity
Progetto del corso di [Ingegneria del Software 2023-2024]
## Utilizzo
Avvio tramite _docker_
`docker-compose up -d `

## Il container clickhouse deve essere riavviato una volta in esecuzione senno non prende le tabelle

Per fermare tutti i container 
`docker-compose down`
Per connettersi a clickhouse con client e ed effettuare query:
`winpty docker exec -it clickhouse clickhouse-client`

Per generare uml:
`pyreverse .\PythonSensorsSimulator\`
 
## Gli UML sono presenti in \UMLModel

## Per avviare speicifici test con possibilita di vedere le print

 `docker exec simulators pytest --capture=no clickHouseDataTest.py`

## Pattern
Simulazioni:
    -Writers : Strategy, Adapter, Composite 
    -Simulator: Template method (simulate), Adapter Misurazione (del modello simulatori) -> Writable(che è il target) (Modello writer)
    -Pool thread: Adpater per la threadpool, Thread pool pattern (non tipico), Adapter anche per gli writable 
    -SimulatorThread: Composite dove il component padre è componentSImulatorThread e la leaf SimulatorThread
