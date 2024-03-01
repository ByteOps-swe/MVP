# InnovaCity

Progetto del corso di [Ingegneria del Software 2023-2024]

## Utilizzo

Avvio tramite _docker_

```bash
docker-compose up -d 
```

Il container clickhouse deve essere riavviato una volta in esecuzione senno non prende le tabelle.

### Accesso dashboard

- Username: admin
- Password: admin

Per fermare tutti i container 

```bash
docker-compose down
```

Per connettersi a clickhouse con client e ed effettuare query:

```bash
winpty docker exec -it clickhouse clickhouse-client
```

Per generare uml:

```bash
pyreverse .\PythonSensorsSimulator\
```
 
## Gli UML sono presenti in \UMLModel

## Per avviare specifici test con possibilità di vedere le print

```bash
docker exec simulators pytest --capture=no clickHouseDataTest.py
```

## Pattern

### Simulazioni:

- Writers: Strategy, Adapter, Composite 
- Simulator: Template method (simulate), Adapter Misurazione (del modello simulatori) -> Writable (che è il target) (Modello writer)
- Pool thread: Adapter per la threadpool, Thread pool pattern (non tipico), Adapter anche per gli writable 
- SimulatorThread: Composite dove il component padre è componentSImulatorThread e la leaf SimulatorThread
