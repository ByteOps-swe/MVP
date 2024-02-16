CREATE TABLE innovacity.chargingStation_kafka (
    timestamp DATETIME64,
    value UInt8,
    type String, --valuterei di toglierlo
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'chargingStation',
    'ch_group_1',
    'JSONEachRow'
);

CREATE TABLE innovacity.chargingStations (
    timestamp DATETIME64,
    value UInt8,
    type String, --valuterei di toglierlo
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = MergeTree()
ORDER BY
    (ID_sensore, timestamp);

CREATE MATERIALIZED VIEW chargingStations_sync TO innovacity.chargingStations AS
SELECT
    *
FROM
    innovacity.chargingStation_kafka;
