CREATE TABLE innovacity.ecoIsland_kafka (
    timestamp DATETIME64,
    value Float32,
    type String, --valuterei di toglierlo
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'ecologicalIsland',
    'ch_group_1',
    'JSONEachRow'
);

CREATE TABLE innovacity.ecoIslands (
    timestamp DATETIME64,
    value Float32,
    type String, --valuterei di toglierlo
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = MergeTree()
ORDER BY
    (ID_sensore, timestamp);

CREATE MATERIALIZED VIEW ecoIsland_sync TO innovacity.ecoIslands AS
SELECT
    *
FROM
    innovacity.ecoIsland_kafka;
