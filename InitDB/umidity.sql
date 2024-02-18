CREATE TABLE innovacity.umidity_kafka (
    timestamp DATETIME64,
    value Float32,
    type String, --valuterei di toglierlo
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'umidity',
    'ch_group_1',
    'JSONEachRow'
);

CREATE MATERIALIZED VIEW innovacity.umidities (
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
FROM innovacity.umidity_kafka
GROUP BY timestamp, ID_sensore, cella,type,longitude,latitude;


-- Aggregazione per minuto
CREATE MATERIALIZED VIEW innovacity.umidities1m (
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value AggregateFunction(avgState, Float32)
) ENGINE = AggregatingMergeTree ORDER BY (timestamp, ID_sensore, cella)
AS SELECT
    toStartOfMinute(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.umidity_kafka
GROUP BY timestamp, ID_sensore, cella;

-- Aggregazione per ora
CREATE MATERIALIZED VIEW innovacity.umidities1o (
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value AggregateFunction(avgState, Float32)
) ENGINE = AggregatingMergeTree ORDER BY (timestamp, ID_sensore, cella)
AS SELECT
    toStartOfHour(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.umidity_kafka
GROUP BY timestamp, ID_sensore, cella;


-- Aggregazione per giorno
CREATE MATERIALIZED VIEW innovacity.umidities1g(
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value AggregateFunction(avgState, Float32)
)
ENGINE = AggregatingMergeTree()
ORDER BY (timestamp, ID_sensore, cella)
AS 
SELECT
    toDate(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.umidity_kafka
GROUP BY timestamp, ID_sensore, cella;

-- Aggregazione per mese
CREATE MATERIALIZED VIEW innovacity.umidities1M(
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value AggregateFunction(avgState, Float32)
)
ENGINE = AggregatingMergeTree()
ORDER BY (timestamp, ID_sensore, cella)
AS 
SELECT
    toStartOfMonth(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.umidity_kafka
GROUP BY timestamp, ID_sensore, cella;

