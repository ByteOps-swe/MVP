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
    'CG_Clickhouse_1',
    'JSONEachRow'
);



CREATE TABLE innovacity.umidities
(
 ID_sensore String,
    cella String,
    timestamp DateTime,
    value AggregateFunction(avgState, Float32),
    latitude Float64,
    longitude Float64,
    PRIMARY KEY (ID_sensore, timestamp)
)
ENGINE = AggregatingMergeTree
ORDER BY(ID_sensore,timestamp, cella,latitude,longitude);


CREATE MATERIALIZED VIEW innovacity.mv_umidities
TO innovacity.umidities
AS SELECT
    toStartOfSecond(timestamp) as timestamp ,
    cella,
    ID_sensore,
    avgState(value) AS value,
    latitude,
    longitude,
FROM innovacity.umidities_kafka
GROUP BY (ID_sensore,timestamp, cella,longitude,latitude);


ALTER TABLE innovacity.umidities ADD PROJECTION tmp_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.umidities MATERIALIZE PROJECTION tmp_sensor_cell_projection;

---------- Aggregazione per minuto--------------
CREATE TABLE innovacity.umidities1m(
    ID_sensore String,
    cella String,
    timestamp DateTime,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
) ENGINE = AggregatingMergeTree ORDER BY (ID_sensore,timestamp, cella);

CREATE MATERIALIZED VIEW innovacity.mv_umidities1m 
TO innovacity.umidities1m
AS SELECT
    toStartOfMinute(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.umidities_kafka
GROUP BY  ID_sensore,timestamp, cella;

ALTER TABLE innovacity.umidities1m ADD PROJECTION tmp_sensor_cell_projection1m (SELECT * ORDER BY cella);

ALTER TABLE innovacity.umidities1m MATERIALIZE PROJECTION tmp_sensor_cell_projection1m;


-- Aggregazione per ora
CREATE TABLE innovacity.umidities1o(
    ID_sensore String,
    cella String,
    timestamp DateTime,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
) ENGINE = AggregatingMergeTree ORDER BY (ID_sensore,timestamp, cella);

CREATE MATERIALIZED VIEW innovacity.mv_umidities1o TO innovacity.umidities1o
AS SELECT
    toStartOfHour(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.umidities_kafka
GROUP BY ID_sensore, timestamp, cella;

ALTER TABLE innovacity.umidities1o ADD PROJECTION tmp_sensor_cell_projection1o (SELECT * ORDER BY cella);

ALTER TABLE innovacity.umidities1o MATERIALIZE PROJECTION tmp_sensor_cell_projection1o;

-- Aggregazione per giorno
CREATE TABLE innovacity.umidities1g(
    ID_sensore String,
    cella String,
    timestamp Date32,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
)
ENGINE = AggregatingMergeTree()
ORDER BY (ID_sensore,timestamp,cella);

CREATE MATERIALIZED VIEW innovacity.mv_umidities1g TO innovacity.umidities1g
AS 
SELECT
    toDate(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.umidities_kafka
GROUP BY  ID_sensore,timestamp, cella;

ALTER TABLE innovacity.umidities1g ADD PROJECTION tmp_sensor_cell_projection1g (SELECT * ORDER BY cella);

ALTER TABLE innovacity.umidities1g MATERIALIZE PROJECTION tmp_sensor_cell_projection1g;

-- Aggregazione per mese
--HO DECISO DI NON CREARE UNA TABELLA CON PROJECTION PERCHE CREDO SIA INUTILE SUI MESI, VISTO CHE NON SI CREERANNO MOLTI DAIT
CREATE MATERIALIZED VIEW innovacity.umidities1M(
    ID_sensore String,
    cella String,
    timestamp Date32,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
)
ENGINE = AggregatingMergeTree()
ORDER BY ( ID_sensore,timestamp, cella)
AS 
SELECT
    toStartOfMonth(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.umidities_kafka
GROUP BY  ID_sensore,timestamp, cella;



