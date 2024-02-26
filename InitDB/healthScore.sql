-- Definizione della tabella "healthScore_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.healthScore_kafka (
    timestamp DATETIME64,
    value Float32,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'HealthScore',
    'CG_Clickhouse_1',
    'JSONEachRow'
);


CREATE TABLE innovacity.healthScore
(
    cella String,
    timestamp DATETIME64,
    value Float32
)
ENGINE = MergeTree()
ORDER BY (cella, timestamp);


CREATE MATERIALIZED VIEW mv_healthScore TO innovacity.healthScore
AS SELECT * FROM innovacity.healthScore_kafka;

