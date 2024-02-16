CREATE TABLE innovacity.umidity_kafka (
    timestamp DATETIME64,
    value Float32,
    type String, --valuterei di toglierlo
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'umidity',
    'ch_group_1',
    'JSONEachRow'
);

CREATE TABLE innovacity.umidities (
    timestamp DATETIME64,
    value Float32,
    type String, --valuterei di toglierlo
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp) -- Partizionamento mensile
ORDER BY
    (ID_sensore, timestamp);
--Partizionamento temporale: Utilizza il partizionamento temporale in base al timestamp per suddividere i dati in partizioni temporali. Questo aiuta a migliorare le --prestazioni delle query che coinvolgono intervalli di tempo specifici, in quanto ClickHouse può eliminare rapidamente le partizioni non rilevanti durante l'esecuzione --della query.

CREATE MATERIALIZED VIEW umidities_sync TO innovacity.umidities AS
SELECT
    *
FROM
    innovacity.umidity_kafka;
