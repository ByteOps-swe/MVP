![build](https://github.com/ByteOps-swe/MVP/actions/workflows/ci.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ByteOps-swe/MVP/badge.svg?branch=main)](https://coveralls.io/github/ByteOps-swe/MVP?branch=main)
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

``` bash
docker exec -it clickhouse clickhouse-client
```

Un possibile fix in caso non funzioni:

``` bash
winpty docker exec -it clickhouse clickhouse-client
```

**TEST**

Per avere print:

``` bash
docker exec simulators pytest
```

``` bash
docker exec simulators pytest --capture=no clickHouseDataTest.py  
```

Per generare uml:

```bash
pyreverse .\PythonSensorsSimulator\
```

Con attributi:
```bash
pyreverse -f ALL .\PythonSensorsSimulator\
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

### Problemi docker su pull immagini locali:

- Se si riscontrano errori *"pull access denied, repository does not exist or may require authorization:"*, provare a risolvere nel seguente modo:  
- Aprire Docker Desktop
- Settings
- Docker Engine
- Aggiungere:
``` JSON
  "features": {  
    "buildkit": false  
  }
```
- Riavviare Docker Desktop