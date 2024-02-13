CREATE TABLE innovacity.rain_queue (
    timestamp DATETIME64,
    value Float32,
    type String,
    latitude Float64,
    longitude Float64,
    nome_sensore String
) ENGINE = Kafka('kafka:9092', 'rain', 'ch_group_1', 'JSONEachRow');


CREATE TABLE innovacity.rain (
    timestamp DATETIME64,
    value Float32,
    type String,
    latitude Float64,
    longitude Float64,
    nome_sensore String
) ENGINE = MergeTree()
ORDER BY (nome_sensore, timestamp);


CREATE MATERIALIZED VIEW rain_consumer_mv TO innovacity.rain
AS SELECT * FROM innovacity.rain_queue;


CREATE TABLE innovacity.rain1m
(
    nome_sensore String,
    timestamp1m DATETIME64,
    avgRain AggregateFunction(avgState, Float32), -- Using sumState for stateful aggregation
    latitude Float64,
    longitude Float64
)
ENGINE = AggregatingMergeTree
ORDER BY (timestamp1m, nome_sensore, longitude, latitude);


CREATE MATERIALIZED VIEW innovacity.rain1m_mv
TO innovacity.rain1m
AS
SELECT
    toStartOfMinute(timestamp) AS timestamp1m,
    nome_sensore,
    avgState(value) as avgRain,
    latitude,
    longitude
FROM innovacity.rain_queue
GROUP BY (timestamp1m, nome_sensore, latitude, longitude);

-- Creare la tabella aggregata
CREATE TABLE innovacity.rain_ma (
    nome_sensore String,
    timestamp1m DATETIME64,
    avgRain Float32,
    latitude Float64,
    longitude Float64
) ENGINE = MergeTree()
ORDER BY (timestamp1m, nome_sensore, latitude, longitude);

-- Creare una Materialized View
CREATE MATERIALIZED VIEW innovacity.rain1m_mov_avg
TO innovacity.rain_ma
AS
SELECT
    nome_sensore,
    toStartOfMinute(timestamp) AS timestamp1m,
    avg(value) OVER (PARTITION BY nome_sensore, toStartOfMinute(timestamp) ORDER BY timestamp1m ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS avgRain,
    latitude,
    longitude
FROM innovacity.rain;
