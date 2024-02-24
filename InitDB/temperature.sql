-- Definizione della tabella "temperatures_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.temperatures_kafka (
    timestamp DATETIME64,
    value Float32,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'temperature',
    'CG_Clickhouse_1',
    'JSONEachRow'
);


CREATE TABLE innovacity.temperatures
(
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value Float32,
    latitude Float64,
    longitude Float64
)
ENGINE = MergeTree()
ORDER BY (ID_sensore, timestamp);


CREATE MATERIALIZED VIEW mv_temperatures TO innovacity.temperatures
AS SELECT * FROM innovacity.temperatures_kafka;

ALTER TABLE innovacity.temperatures ADD PROJECTION tmp_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.temperatures MATERIALIZE PROJECTION tmp_sensor_cell_projection;
