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
    'CG_Clickhouse_1'
) SETTINGS kafka_format = 'JSONEachRow',
           kafka_skip_broken_messages = 10;

CREATE TABLE innovacity.ecoIslands
(
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value Float32,
    latitude Float64,
    longitude Float64
)
ENGINE = MergeTree()
PRIMARY KEY (ID_sensore,toStartOfHour(timestamp), timestamp)
TTL toDateTime(timestamp) + INTERVAL 1 MONTH
    GROUP BY ID_sensore,toStartOfHour(timestamp)
    SET
        value = avg(value);



CREATE MATERIALIZED VIEW mv_ecoIslands TO innovacity.ecoIslands
AS SELECT * FROM innovacity.ecoIslands_kafka
    WHERE (value >= 0 and value <= 100);

ALTER TABLE innovacity.ecoIslands ADD PROJECTION umd_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.ecoIslands MATERIALIZE PROJECTION umd_sensor_cell_projection;
