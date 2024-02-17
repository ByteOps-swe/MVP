-- Definizione della tabella "temperatures_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.temperatures_kafka (
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
    ID_sensore String, -- ID del sensore che ha registrato la temperatura
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'temperature',
    'ch_group_1',
    'JSONEachRow'
);

-- Utilizzo del motore Kafka per leggere i dati
-- Definizione della tabella "temperatures" che conterrà i dati di temperatura consolidati
CREATE MATERIALIZED VIEW innovacity.temperatures (
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value AggregateFunction(avgState, Float32),
    type String,
    latitude Float64,
    longitude Float64
) ENGINE = AggregatingMergeTree ORDER BY (timestamp, ID_sensore, cella,latitude,longitude,type)
AS SELECT
    toStartOfSecond(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value,
    latitude,
    longitude,
    type
FROM innovacity.temperatures_kafka
GROUP BY timestamp, ID_sensore, cella,type,longitude,latitude;


-- Creazione della Materialized View `temperatures1m_mv`
CREATE MATERIALIZED VIEW innovacity.temperatures1m (
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value AggregateFunction(avgState, Float32)
) ENGINE = ReplacingMergeTree ORDER BY (timestamp, ID_sensore, cella)  --CON REPLACING FUNZIONA BENE CAVOLOOOOO MA NON SAREBBE QUELLO ADEGUATO
AS SELECT
    toStartOfMinute(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.temperatures_kafka
GROUP BY timestamp, ID_sensore, cella;


CREATE MATERIALIZED VIEW innovacity.temperatures1g(
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value AggregateFunction(avgState, Float32)
)
ENGINE = ReplacingMergeTree()
ORDER BY (timestamp, ID_sensore, cella)
AS 
SELECT
    toDate(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.temperatures_kafka
GROUP BY timestamp, ID_sensore, cella;


CREATE MATERIALIZED VIEW innovacity.temperatures1M(
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value AggregateFunction(avgState, Float32)
)
ENGINE = ReplacingMergeTree()
ORDER BY (timestamp, ID_sensore, cella)
AS 
SELECT
    toStartOfMonth(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.temperatures_kafka
GROUP BY timestamp, ID_sensore, cella;

