-- Definizione della tabella "temperatures_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.temperatures_kafka (
    timestamp DATETIME64,
    value Float32,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'temperature',
    'CG_Clickhouse_1',
    'JSONEachRow'
);

CREATE TABLE innovacity.temperatures
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
PARTITION BY toYYYYMMDD(timestamp)  -- Partition basata sul giorno corrente
ORDER BY(ID_sensore,timestamp, cella,latitude,longitude);


CREATE MATERIALIZED VIEW innovacity.mv_temperatures
TO innovacity.temperatures
AS SELECT
    toStartOfSecond(timestamp) as timestamp ,
    cella,
    ID_sensore,
    avgState(value) AS value,
    latitude,
    longitude,
FROM innovacity.temperatures_kafka
GROUP BY (ID_sensore,timestamp, cella,longitude,latitude);


ALTER TABLE innovacity.temperatures ADD PROJECTION umd_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.temperatures MATERIALIZE PROJECTION umd_sensor_cell_projection;

---------- Aggregazione per minuto--------------
CREATE TABLE innovacity.temperatures1m(
    ID_sensore String,
    cella String,
    timestamp DateTime,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
) ENGINE = AggregatingMergeTree ORDER BY (ID_sensore,timestamp, cella);

CREATE MATERIALIZED VIEW innovacity.mv_temperatures1m 
TO innovacity.temperatures1m
AS SELECT
    toStartOfMinute(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.temperatures_kafka
GROUP BY  ID_sensore,timestamp, cella;

ALTER TABLE innovacity.temperatures1m ADD PROJECTION umd_sensor_cell_projection1m (SELECT * ORDER BY cella);

ALTER TABLE innovacity.temperatures1m MATERIALIZE PROJECTION umd_sensor_cell_projection1m;


-- Aggregazione per ora
CREATE TABLE innovacity.temperatures1o(
    ID_sensore String,
    cella String,
    timestamp DateTime,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
) ENGINE = AggregatingMergeTree ORDER BY (ID_sensore,timestamp, cella);

CREATE MATERIALIZED VIEW innovacity.mv_temperatures1o TO innovacity.temperatures1o
AS SELECT
    toStartOfHour(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.temperatures_kafka
GROUP BY ID_sensore, timestamp, cella;

ALTER TABLE innovacity.temperatures1o ADD PROJECTION umd_sensor_cell_projection1o (SELECT * ORDER BY cella);

ALTER TABLE innovacity.temperatures1o MATERIALIZE PROJECTION umd_sensor_cell_projection1o;

-- Aggregazione per giorno
CREATE TABLE innovacity.temperatures1g(
    ID_sensore String,
    cella String,
    timestamp Date32,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
)
ENGINE = AggregatingMergeTree()
ORDER BY (ID_sensore,timestamp,cella);

CREATE MATERIALIZED VIEW innovacity.mv_temperatures1g TO innovacity.temperatures1g
AS 
SELECT
    toDate(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.temperatures_kafka
GROUP BY  ID_sensore,timestamp, cella;

ALTER TABLE innovacity.temperatures1g ADD PROJECTION umd_sensor_cell_projection1g (SELECT * ORDER BY cella);

ALTER TABLE innovacity.temperatures1g MATERIALIZE PROJECTION umd_sensor_cell_projection1g;

-- Aggregazione per mese
--HO DECISO DI NON CREARE UNA TABELLA CON PROJECTION PERCHE CREDO SIA INUTILE SUI MESI, VISTO CHE NON SI CREERANNO MOLTI DAIT
CREATE MATERIALIZED VIEW innovacity.temperatures1M(
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
FROM innovacity.temperatures_kafka
GROUP BY  ID_sensore,timestamp, cella;



