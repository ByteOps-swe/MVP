CREATE TABLE innovacity.test_kafka (
    timestamp DATETIME64(6),
    value Float32,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'test',
    'CG_Clickhouse_1')
SETTINGS  kafka_format = 'JSONEachRow',
            kafka_skip_broken_messages = 65536,
            kafka_max_block_size = 65536 ;

CREATE TABLE innovacity.test
(
    ID_sensore String,
    cella String,
    timestamp DATETIME64(6),
    value Float32,
    latitude Float64,
    longitude Float64,
    arrival_timestamp DateTime64(6) DEFAULT now64(6)
)
ENGINE = MergeTree()
ORDER BY (ID_sensore, timestamp);


CREATE MATERIALIZED VIEW mv_test TO innovacity.test
AS SELECT * FROM innovacity.test_kafka;
