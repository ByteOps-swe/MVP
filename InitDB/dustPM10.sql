-- Definizione della tabella "dustPM10_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.dustPM10_kafka (
    timestamp DATETIME64(6),
    value Float32,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'dust_PM10',
    'CG_Clickhouse_1'
) SETTINGS kafka_format = 'JSONEachRow',
           kafka_skip_broken_messages = 10;


CREATE TABLE innovacity.dust_PM10
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


CREATE MATERIALIZED VIEW mv_dust_PM10 TO innovacity.dust_PM10
AS SELECT * FROM innovacity.dustPM10_kafka 
    WHERE (value >= 0 AND value <= 150);

ALTER TABLE innovacity.dust_PM10 ADD PROJECTION dust_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.dust_PM10 MATERIALIZE PROJECTION dust_sensor_cell_projection;
