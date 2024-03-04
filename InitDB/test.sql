CREATE TABLE innovacity.test_kafka (
    timestamp DATETIME64,
    value Float32,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'test',
    'CG_Clickhouse_1',
    'JSONEachRow'
);


CREATE TABLE innovacity.test
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


CREATE MATERIALIZED VIEW mv_test TO innovacity.test
AS SELECT * FROM innovacity.test_kafka;
