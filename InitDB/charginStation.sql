-- Definizione della tabella "temperatures_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.chargingStation_kafka (
    timestamp DATETIME64,
    -- Timestamp della rilevazione
    value UInt8,
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
    'chargingStation',
    'ch_group_1',
    'JSONEachRow'
);

-- Utilizzo del motore Kafka per leggere i dati
-- Definizione della tabella "temperatures" che conterrà i dati di temperatura consolidati
CREATE TABLE innovacity.chargingStations (
    timestamp DATETIME64,
    -- Timestamp della rilevazione
    value UInt8,
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

CREATE MATERIALIZED VIEW chargingStations_sync TO innovacity.chargingStations AS
SELECT
    *
FROM
    innovacity.chargingStation_kafka;
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