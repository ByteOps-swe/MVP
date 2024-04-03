-- Definizione della tabella "humidity_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.humidity_kafka (
    timestamp DATETIME64(6),
    value Float32,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'humidity',
    'CG_Clickhouse_1'
) SETTINGS  kafka_format = 'JSONEachRow',
            kafka_skip_broken_messages = 65536,
            kafka_max_block_size = 65536 ;

CREATE TABLE innovacity.humidity
(
    ID_sensore String,
    cella String,
    timestamp DATETIME64(6),
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


CREATE MATERIALIZED VIEW mv_humidity TO innovacity.humidity
AS SELECT * FROM innovacity.humidity_kafka
    WHERE (value >= 0 AND value <= 100);

ALTER TABLE innovacity.humidity ADD PROJECTION umd_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.humidity MATERIALIZE PROJECTION umd_sensor_cell_projection;
