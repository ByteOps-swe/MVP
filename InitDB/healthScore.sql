-- Definizione della tabella "healthScore_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.healthScore_kafka (
    timestamp DATETIME64(6),
    value Float32,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'HealthScore',
    'CG_Clickhouse_1'
) SETTINGS  kafka_format = 'JSONEachRow',
            kafka_skip_broken_messages = 65536,
            kafka_max_block_size = 65536 ;
--kafka_max_block_size (default 65536) — the threshold to commit the block to ClickHouse in number of rows, configured on a table level

CREATE TABLE innovacity.healthScore
(
    cella String,
    timestamp DATETIME64(6),
    value Float32
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp) 
PRIMARY KEY (cella,toStartOfHour(timestamp), timestamp)
TTL toDateTime(timestamp) + INTERVAL 1 MONTH
    GROUP BY cella,toStartOfHour(timestamp)
    SET
        value = avg(value);


CREATE MATERIALIZED VIEW mv_healthScore TO innovacity.healthScore
AS SELECT * FROM innovacity.healthScore_kafka;

