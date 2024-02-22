CREATE TABLE innovacity.chargingStation_kafka (
    timestamp DATETIME64,
    value UInt8,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'chargingStation',
    'CG_Clickhouse_1',
    'JSONEachRow'
);

CREATE TABLE innovacity.chargingStations (
    timestamp DATETIME64,
    value UInt8,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String,
    PRIMARY KEY (ID_sensore, timestamp)
) ENGINE = MergeTree()
ORDER BY
    (ID_sensore, timestamp);

CREATE MATERIALIZED VIEW chargingStations_sync TO innovacity.chargingStations AS
SELECT
    *
FROM
    innovacity.chargingStation_kafka;

ALTER TABLE innovacity.chargingStations ADD PROJECTION chStation_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.chargingStations MATERIALIZE PROJECTION chStation_sensor_cell_projection;