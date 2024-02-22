CREATE TABLE innovacity.chargingStation_kafka (
    timestamp DATETIME64,
    value UInt8,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'chargingStation',
    'CG_Clickhouse_1',
    'JSONEachRow'
);

CREATE TABLE innovacity.chargingStations (
    timestamp DATETIME64,
    value UInt8,
    latitude Float64,
    longitude Float64,
    ID_sensore String,
    cella String,
    PRIMARY KEY (ID_sensore, timestamp)
) ENGINE = MergeTree()
ORDER BY
    (ID_sensore, timestamp);

CREATE MATERIALIZED VIEW chargingStations_sync TO innovacity.chargingStations AS
SELECT
    *
FROM
    innovacity.chargingStation_kafka;

ALTER TABLE innovacity.chargingStations ADD PROJECTION chStation_sensor_cell_projection (SELECT * ORDER BY cella);

ALTER TABLE innovacity.chargingStations MATERIALIZE PROJECTION chStation_sensor_cell_projection;


SELECT ID_sensore, value, timestamp FROM (
    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp,
        'Secondo' AS Aggr
    FROM
        innovacity.temperatures
    WHERE
        cella IN ($Cella)
        AND (
            Aggr = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) >= 0
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 300
                )
            )
        )
    GROUP BY timestamp, ID_sensore

    UNION ALL

    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp,
        'Minuto' AS Aggr
    FROM
        innovacity.temperatures1m
    WHERE
        cella IN ($Cella)
        AND (
            Aggr = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 300
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 3600
                )
            )
        )
    GROUP BY timestamp, ID_sensore

    UNION ALL

    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp,
        'Ora' AS Aggr
    FROM
        innovacity.temperatures1o
    WHERE
        cella IN ($Cella)
        AND (
            Aggr = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 3600
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 86400
                )
            )
        )
    GROUP BY timestamp, ID_sensore

    UNION ALL

    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp,
        'Giorno' AS Aggr
    FROM
        innovacity.temperatures1g
    WHERE
        cella IN ($Cella)
        AND (
            Aggr = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 86400
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 2592000
                )
            )
        )
    GROUP BY timestamp, ID_sensore

    UNION ALL

    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp,
        'Mese' AS Aggr
    FROM
        innovacity.temperatures1M
    WHERE
        cella IN ($Cella)
        AND (
            Aggr = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 2592000
                )
            )
        )
    GROUP BY timestamp, ID_sensore
) 
WHERE
    value >= ($MinTemperature)
    AND value <= ($MaxTemperature)
    AND (
        timestamp >= $__fromTime
        AND timestamp <= $__toTime
    )
    AND ID_sensore IN ($tmp_sensors_id)