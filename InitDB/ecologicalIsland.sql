CREATE TABLE innovacity.ecoIslands_kafka (
    timestamp DATETIME64,
    value Float32,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'ecologicalIsland',
    'CG_Clickhouse_1',
    'JSONEachRow'
);



CREATE TABLE innovacity.ecoIslands
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


CREATE MATERIALIZED VIEW innovacity.mv_ecoIslands
TO innovacity.ecoIslands
AS SELECT
    toStartOfSecond(timestamp) as timestamp ,
    cella,
    ID_sensore,
    avgState(value) AS value,
    latitude,
    longitude,
FROM innovacity.ecoIslands_kafka
GROUP BY (ID_sensore,timestamp, cella,longitude,latitude);


ALTER TABLE innovacity.ecoIslands ADD PROJECTION tmp_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.ecoIslands MATERIALIZE PROJECTION tmp_sensor_cell_projection;

---------- Aggregazione per minuto--------------
CREATE TABLE innovacity.ecoIslands1m(
    ID_sensore String,
    cella String,
    timestamp DateTime,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
) ENGINE = AggregatingMergeTree ORDER BY (ID_sensore,timestamp, cella);

CREATE MATERIALIZED VIEW innovacity.mv_ecoIslands1m 
TO innovacity.ecoIslands1m
AS SELECT
    toStartOfMinute(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.ecoIslands_kafka
GROUP BY  ID_sensore,timestamp, cella;

ALTER TABLE innovacity.ecoIslands1m ADD PROJECTION tmp_sensor_cell_projection1m (SELECT * ORDER BY cella);

ALTER TABLE innovacity.ecoIslands1m MATERIALIZE PROJECTION tmp_sensor_cell_projection1m;


-- Aggregazione per ora
CREATE TABLE innovacity.ecoIslands1o(
    ID_sensore String,
    cella String,
    timestamp DateTime,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
) ENGINE = AggregatingMergeTree ORDER BY (ID_sensore,timestamp, cella);

CREATE MATERIALIZED VIEW innovacity.mv_ecoIslands1o TO innovacity.ecoIslands1o
AS SELECT
    toStartOfHour(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.ecoIslands_kafka
GROUP BY ID_sensore, timestamp, cella;

ALTER TABLE innovacity.ecoIslands1o ADD PROJECTION tmp_sensor_cell_projection1o (SELECT * ORDER BY cella);

ALTER TABLE innovacity.ecoIslands1o MATERIALIZE PROJECTION tmp_sensor_cell_projection1o;

-- Aggregazione per giorno
CREATE TABLE innovacity.ecoIslands1g(
    ID_sensore String,
    cella String,
    timestamp Date32,
    value AggregateFunction(avgState, Float32),
    PRIMARY KEY (ID_sensore, timestamp)
)
ENGINE = AggregatingMergeTree()
ORDER BY (ID_sensore,timestamp,cella);

CREATE MATERIALIZED VIEW innovacity.mv_ecoIslands1g TO innovacity.ecoIslands1g
AS 
SELECT
    toDate(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avgState(value) AS value
FROM innovacity.ecoIslands_kafka
GROUP BY  ID_sensore,timestamp, cella;

ALTER TABLE innovacity.ecoIslands1g ADD PROJECTION tmp_sensor_cell_projection1g (SELECT * ORDER BY cella);

ALTER TABLE innovacity.ecoIslands1g MATERIALIZE PROJECTION tmp_sensor_cell_projection1g;

-- Aggregazione per mese
--HO DECISO DI NON CREARE UNA TABELLA CON PROJECTION PERCHE CREDO SIA INUTILE SUI MESI, VISTO CHE NON SI CREERANNO MOLTI DAIT
CREATE MATERIALIZED VIEW innovacity.ecoIslands1M(
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
FROM innovacity.ecoIslands_kafka
GROUP BY  ID_sensore,timestamp, cella;



