# InnovaCity
Progetto del corso di [Ingegneria del Software 2023-2024]
## Utilizzo

Avvio tramite _docker_

`docker-compose up -d `

Per fermare tutti i container 

`docker-compose down`

Per connettersi a clichouse con client e ed effettuare query:
`winpty docker exec -it clickhouse clickhouse-client`