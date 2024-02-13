# InnovaCity
Progetto del corso di [Ingegneria del Software 2023-2024](https://didattica.unipd.it/off/2021/LT/SC/SC1167/000ZZ/SC01103936/N0) @ [Università degli Studi di Padova](https://www.unipd.it)

**Proponente:** [SyncLab](https://www.synclab.it/)

**Proposta:** Realizzazione di una architettura software in grado di ingerire, immagazzinare ed analizzare grandi quantità di dati provenienti da device IoT.

## Utilizzo

Per l'avvio tramite _docker_, dell'intero stack, utilizzare il comando

`docker-compose --profile prod up -d `

Secondo le necessità si possono aggiungere le flag `--force-recreate` e `--build`.

Se si vuole avviare solamente la _data pipeline_, e lanciare il simulatore in locale (per esempio durante lo sviluppo), è
sufficiente utilzzare il comando 

`docker-compose --profile dev up -d`,

aggiungendo anche qui le flag secondo le necessità.

Per fermare tutti i container utilizzare rispettivamente i comandi

`docker-compose --profile prod down`

`docker-compose --profile dev down`

## Accesso
Le credenziali per l'accesso a Grafana username e password sono rispettivamente `ic_admin` e `ic_admin`.
