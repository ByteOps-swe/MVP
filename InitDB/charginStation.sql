CREATE TABLE innovacity.chargingStations_kafka (
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


CREATE TABLE innovacity.chargingStations
(
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value UInt8,
    latitude Float64,
    longitude Float64
)
ENGINE = MergeTree()
ORDER BY (ID_sensore, timestamp);


CREATE MATERIALIZED VIEW mv_chargingStations TO innovacity.chargingStations
AS SELECT * FROM innovacity.chargingStations_kafka;

ALTER TABLE innovacity.chargingStations ADD PROJECTION chS_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.chargingStations MATERIALIZE PROJECTION chS_sensor_cell_projection;
