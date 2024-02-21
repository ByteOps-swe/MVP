-- Definizione della tabella "ecoIslands_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.ecoIslands_kafka (
    timestamp DATETIME64,
    value Float32,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'ecologicalIsland',
    'CG_Clickhouse_1',
    'JSONEachRow'
);

CREATE TABLE innovacity.ecoIslands
(
 ID_sensore String,
    cella String,
    timestamp DateTime,
    value AggregateFunction(avgState, Float32),
    latitude Float64,
    longitude Float64,
    PRIMARY KEY (ID_sensore, timestamp)
)
ENGINE = AggregatingMergeTree
PARTITION BY toYYYYMMDD(timestamp)  -- Partition basata sul giorno corrente
ORDER BY(ID_sensore,timestamp, cella,latitude,longitude);


CREATE MATERIALIZED VIEW innovacity.mv_ecoIslands
TO innovacity.ecoIslands
AS SELECT
    toStartOfSecond(timestamp) as timestamp ,
    cella,
    ID_sensore,
    avgState(value) AS value,
    latitude,
    longitude,
FROM innovacity.ecoIslands_kafka
GROUP BY (ID_sensore,timestamp, cella,longitude,latitude);

ALTER TABLE innovacity.ecoIslands ADD PROJECTION ecoIs_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.ecoIslands MATERIALIZE PROJECTION ecoIs_sensor_cell_projection;