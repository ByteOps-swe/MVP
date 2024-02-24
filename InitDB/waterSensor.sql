CREATE TABLE innovacity.waterPresence_kafka (
    timestamp DATETIME64,
    value UInt8,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'waterPresence',
    'CG_Clickhouse_1',
    'JSONEachRow'
);


CREATE TABLE innovacity.waterPresence
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


CREATE MATERIALIZED VIEW mv_waterPresence TO innovacity.waterPresence
AS SELECT * FROM innovacity.waterPresence_kafka;

ALTER TABLE innovacity.waterPresence ADD PROJECTION waPr_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.waterPresence MATERIALIZE PROJECTION waPr_sensor_cell_projection;
