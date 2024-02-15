-- Definizione della tabella "temperatures_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.umidity_kafka (
    timestamp DATETIME64,
    -- Timestamp della rilevazione
    value Float32,
    -- Valore della temperatura
    type String,
    -- Tipo di temperatura (potrebbe essere utile per eventuali distinzioni)
    latitude Float64,
    -- Latitudine della posizione del sensore
    longitude Float64,
    -- Longitudine della posizione del sensore
    ID_sensore String -- ID del sensore che ha registrato la temperatura
) ENGINE = Kafka(
    'kafka:9092',
    'umidity',
    'ch_group_1',
    'JSONEachRow'
);

-- Utilizzo del motore Kafka per leggere i dati
-- Definizione della tabella "temperatures" che conterrà i dati di temperatura consolidati
CREATE TABLE innovacity.umidities (
    timestamp DATETIME64,
    -- Timestamp della rilevazione
    value Float32,
    -- Valore della temperatura
    type String,
    -- Tipo di temperatura
    latitude Float64,
    -- Latitudine della posizione del sensore
    longitude Float64,
    -- Longitudine della posizione del sensore
    ID_sensore String -- Nome del sensore
) ENGINE = MergeTree() -- Utilizzo del motore MergeTree per l'archiviazione ottimizzata
ORDER BY
    (ID_sensore, timestamp);

-- La scelta di utilizzare il motore MergeTree e l'ordinamento per nome_sensore e timestamp ha diverse ragioni:
-- Efficienza nella lettura dei dati: ClickHouse è progettato per eseguire operazioni analitiche ad alte prestazioni su grandi volumi di dati. L'ordinamento dei dati sulla chiave nome_sensore e timestamp consente al sistema di eseguire interrogazioni di lettura in modo efficiente, specialmente quando si richiedono dati per un determinato sensore o per un intervallo di tempo specifico.
-- Ricerca e filtraggio efficiente: Quando i dati sono ordinati per nome_sensore e timestamp, le query che filtrano i dati per un sensore specifico o per un intervallo di tempo possono eliminare rapidamente le parti dei dati che non sono rilevanti per la query, migliorando notevolmente le prestazioni.
-- Aggregazione e analisi semplificate: L'ordinamento dei dati per timestamp può semplificare l'analisi dei dati temporali, consentendo di eseguire facilmente operazioni di aggregazione e calcoli su finestre temporali specifiche.
-- In sostanza, l'uso del motore MergeTree con l'ordinamento specificato è una scelta strategica per ottimizzare le prestazioni delle query e migliorare l'efficienza complessiva nel processo di archiviazione e interrogazione dei dati delle temperature.
-- Ordinamento dei dati per nome del sensore e timestamp
-- Creazione di una Materialized View per sincronizzare i dati da "temperatures_kafka" a "temperatures"
CREATE MATERIALIZED VIEW umidities_sync TO innovacity.umidities AS
SELECT
    *
FROM
    innovacity.umidity_kafka;
/*
-- Definizione della tabella "temperatures1m" per i dati aggregati per minuto
CREATE TABLE innovacity.temperatures1m (
    ID_sensore String,
    timestamp1m DATETIME64,
    avgTemperature Float32,
    latitude Float64,
    longitude Float64
) ENGINE = AggregatingMergeTree
ORDER BY (timestamp1m, ID_sensore, longitude, latitude);

-- Ordinamento dei dati per timestamp, nome del sensore e posizione
-- Creazione di una Materialized View per calcolare le medie delle temperature ogni minuto
CREATE MATERIALIZED VIEW innovacity.temperatures1m_mv TO innovacity.temperatures1m AS
SELECT
    toStartOfMinute(timestamp) AS timestamp1m,
    -- Inizio del minuto per il timestamp
    ID_sensore,
    -- Nome del sensore
    avgState(value) as avgTemperature,
    -- Calcolo della media delle temperature
    latitude,
    -- Latitudine della posizione del sensore
    longitude -- Longitudine della posizione del sensore
FROM
    innovacity.temperatures
GROUP BY
    (timestamp1m, ID_sensore, latitude, longitude);

-- ! TOGLIEREI LATITUDE E LONGITUDE TANTO C è ID SENSORE

 -- Raggruppamento per timestamp, nome del sensore e posizione
 -- Definizione della tabella "temperatures_ma" per le medie mobili delle temperature
 CREATE TABLE innovacity.temperatures_ma (
 ID_sensore String,
 -- Nome del sensore
 timestamp1m DATETIME64,
 -- Timestamp raggruppato per minuto
 avgTemperature Float32,
 -- Media mobile delle temperature
 latitude Float64,
 -- Latitudine della posizione del sensore
 longitude Float64 -- Longitudine della posizione del sensore
 ) ENGINE = MergeTree() -- Utilizzo del motore MergeTree per l'archiviazione ottimizzata
 ORDER BY
 (timestamp1m, ID_sensore, latitude, longitude);
 
 -- Ordinamento dei dati per timestamp, nome del sensore e posizione
 -- Creazione di una Materialized View per calcolare le medie mobili delle temperature
 CREATE MATERIALIZED VIEW innovacity.temperatures1m_mov_avg TO innovacity.temperatures_ma AS
 SELECT
 ID_sensore,
 -- Nome del sensore
 toStartOfMinute(timestamp) AS timestamp1m,
 -- Inizio del minuto per il timestamp
 avg(value) OVER (
 PARTITION BY toStartOfMinute(timestamp)
 ORDER BY
 timestamp1m ROWS BETWEEN 2 PRECEDING
 AND CURRENT ROW
 ) AS avgTemperature,
 -- Calcolo della media mobile delle temperature
 latitude,
 -- Latitudine della posizione del sensore
 longitude -- Longitudine della posizione del sensore
 FROM
 innovacity.temperatures;
 */