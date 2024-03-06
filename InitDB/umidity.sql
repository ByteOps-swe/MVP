-- Definizione della tabella "umidities_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.umidities_kafka (
    timestamp DATETIME64,
    value Float32,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'umidity',
    'CG_Clickhouse_1'
) SETTINGS kafka_format = 'JSONEachRow',
           kafka_skip_broken_messages = 10;


CREATE TABLE innovacity.umidities
(
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value Float32,
    latitude Float64,
    longitude Float64
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp) 
PRIMARY KEY (ID_sensore,toStartOfHour(timestamp), timestamp)
TTL toDateTime(timestamp) + INTERVAL 1 MONTH
    GROUP BY ID_sensore,toStartOfHour(timestamp)
    SET
        value = avg(value);


CREATE MATERIALIZED VIEW mv_umidities TO innovacity.umidities
AS SELECT * FROM innovacity.umidities_kafka;

ALTER TABLE innovacity.umidities ADD PROJECTION umd_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.umidities MATERIALIZE PROJECTION umd_sensor_cell_projection;
