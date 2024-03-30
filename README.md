<div align="center">

![build](https://github.com/ByteOps-swe/MVP/actions/workflows/ci.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ByteOps-swe/MVP/badge.svg?branch=main)](https://coveralls.io/github/ByteOps-swe/MVP?branch=main)
[![codecov](https://codecov.io/gh/ByteOps-swe/MVP/graph/badge.svg?token=VSRO4CTN60)](https://codecov.io/gh/ByteOps-swe/MVP/tree/main)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/68c20d2874784c78bf7e4ebcb51aba95)](https://app.codacy.com/gh/ByteOps-swe/MVP/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)\
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
![pylint](https://img.shields.io/badge/PyLint-9.76-brightgreen?logo=python&logoColor=white)

</div>

# InnovaCity

Progetto del corso di [Ingegneria del Software 2023-2024]

## Utilizzo

Avvio tramite _docker_

```bash
docker compose --profile prod up -d 
```

### Accesso dashboard
## Admin
- Username: admin
- Password: admin
## User
- Username: user
- Password: user
  
Per fermare tutti i container

```bash
docker compose --profile prod down
```
<!-- docekr exec clickhouse dovrebe essere tolta mi pare -->
Per connettersi a clickhouse con client e ed effettuare query:

``` bash
docker exec -it clickhouse clickhouse-client
```

Un possibile fix in caso non funzioni:

``` bash
winpty docker exec -it clickhouse clickhouse-client
```

**TEST**

Per eseguire i test automaticamente:

``` bash
docker compose --profile test up -d
```

Per riavviare il container dei test:

``` bash
docker restart tests
```

Per avviare specifici test

```bash
docker exec tests pytest <file_path>
```

Per avviare specifici test con possibilità di vedere le print

```bash
docker exec tests pytest --capture=no <file_path>
```
 
## Gli UML sono presenti in \UMLModel

Per generare uml:

```bash
pyreverse <folder_path>
```

Con attributi:
```bash
pyreverse -f ALL <folder_path>
```


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
