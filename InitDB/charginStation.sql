CREATE TABLE innovacity.chargingStations_kafka (
    timestamp DATETIME64(6),
    value UInt8, --Type bool is internally stored as UInt8
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'chargingStation',
    'CG_Clickhouse_1'
) SETTINGS  kafka_format = 'JSONEachRow',
            kafka_skip_broken_messages = 65536,
            kafka_max_block_size = 65536 ;


CREATE TABLE innovacity.chargingStations
(
    ID_sensore String,
    cella String,
    timestamp DATETIME64(6),
    value UInt8,
    latitude Float64,
    longitude Float64
)
ENGINE = MergeTree()
ORDER BY (ID_sensore, timestamp);


CREATE MATERIALIZED VIEW mv_chargingStations TO innovacity.chargingStations
AS SELECT * FROM innovacity.chargingStations_kafka 
    WHERE (value = 0 or value = 1);

