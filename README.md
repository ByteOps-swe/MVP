![build](https://github.com/ByteOps-swe/MVP/actions/workflows/ci.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ByteOps-swe/MVP/badge.svg?branch=main)](https://coveralls.io/github/ByteOps-swe/MVP?branch=main)
[![codecov](https://codecov.io/gh/ByteOps-swe/MVP/graph/badge.svg?token=VSRO4CTN60)](https://codecov.io/gh/ByteOps-swe/MVP)\
[![Maintainability](https://api.codeclimate.com/v1/badges/a8e8861f6abf888a6552/maintainability)](https://codeclimate.com/github/ByteOps-swe/MVP/maintainability)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/68c20d2874784c78bf7e4ebcb51aba95)](https://app.codacy.com/gh/ByteOps-swe/MVP/tree/Repo-badge/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
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

TEST
`docker exec simulators pytest`
docker exec simulators pytest --capture=no clickHouseDataTest.py
per avere print

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
  "features": {  
    "buildkit": false  
  }
- Riavviare Docker Desktop