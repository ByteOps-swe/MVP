--UMIDITY
SELECT 
    ID_sensore, 
     value , 
    timestamp 
FROM (
    SELECT
        ID_sensore as ID_sensore,
        avgMerge(value) as value,
        timestamp as timestamp,
        'Secondo' as Aggr
    FROM
        innovacity.umidities
    WHERE 
        cella IN ($Cella) 
        AND (timestamp >= $__fromTime AND timestamp <= $__toTime) 
        AND ID_sensore IN ($umd_sensors_id) 
        AND (
            Aggr = '${AggregazioneTemporale}' OR
            (
                '${AggregazioneTemporale}' = 'Automatico' AND
                (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) >= 0 
                    AND 
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 300
                )
            )
        )
    GROUP BY 
        timestamp, 
        ID_sensore
    HAVING 
        value >= ($MinUmidity) 
        AND value <= ($MaxUmidity)
) AS subquery_alias;

SELECT 
    ID_sensore, 
     value , 
    timestamp 
FROM (
    SELECT
        ID_sensore as ID_sensore,
        avgMerge(value) as value,
        timestamp as timestamp,
        'Minuto' as Aggr
    FROM
        innovacity.umidities1m
    WHERE 
        cella IN ($Cella) 
        AND (timestamp >= $__fromTime AND timestamp <= $__toTime) 
        AND ID_sensore IN ($umd_sensors_id) 
        AND (
            Aggr = '${AggregazioneTemporale}' OR
            (
                '${AggregazioneTemporale}' = 'Automatico' AND
                (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 300 
                    AND 
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 3600
                )
            )
        )
    GROUP BY 
        timestamp, 
        ID_sensore
    HAVING 
        value >= ($MinUmidity) 
        AND value <= ($MaxUmidity)
) AS subquery_alias;

SELECT 
    ID_sensore, 
     value , 
    timestamp 
FROM (
    SELECT
        ID_sensore as ID_sensore,
        avgMerge(value) as value,
        timestamp as timestamp,
        'Ora' as Aggr
    FROM
        innovacity.umidities1o
    WHERE 
        cella IN ($Cella) 
        AND (timestamp >= $__fromTime AND timestamp <= $__toTime) 
        AND ID_sensore IN ($umd_sensors_id) 
        AND (
            Aggr = '${AggregazioneTemporale}' OR
            (
                '${AggregazioneTemporale}' = 'Automatico' AND
                (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 3600
                    AND 
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 86400
                )
            )
        )
    GROUP BY 
        timestamp, 
        ID_sensore
    HAVING 
        value >= ($MinUmidity) 
        AND value <= ($MaxUmidity)
) AS subquery_alias;

SELECT 
    ID_sensore, 
     value , 
    timestamp 
FROM (
    SELECT
        ID_sensore as ID_sensore,
        avgMerge(value) as value,
        timestamp as timestamp,
        'Giorno' as Aggr
    FROM
        innovacity.umidities1g
    WHERE 
        cella IN ($Cella) 
        AND (timestamp >= $__fromTime AND timestamp <= $__toTime) 
        AND ID_sensore IN ($umd_sensors_id) 
        AND (
            Aggr = '${AggregazioneTemporale}' OR
            (
                '${AggregazioneTemporale}' = 'Automatico' AND
                (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 86400
                    AND 
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 2592000
                )
            )
        )
    GROUP BY 
        timestamp, 
        ID_sensore
    HAVING 
        value >= ($MinUmidity) 
        AND value <= ($MaxUmidity)
) AS subquery_alias;

SELECT 
    ID_sensore, 
     value , 
    timestamp 
FROM (
    SELECT
        ID_sensore as ID_sensore,
        avgMerge(value) as value,
        timestamp as timestamp,
        'Mese' as Aggr
    FROM
        innovacity.umidities1M
    WHERE 
        cella IN ($Cella) 
        AND (timestamp >= $__fromTime AND timestamp <= $__toTime) 
        AND ID_sensore IN ($umd_sensors_id) 
        AND (
            Aggr = '${AggregazioneTemporale}' OR
            (
                '${AggregazioneTemporale}' = 'Automatico' AND
                (
                   
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 2592000
                )
            )
        )
    GROUP BY 
        timestamp, 
        ID_sensore
    HAVING 
        value >= ($MinUmidity) 
        AND value <= ($MaxUmidity)
) AS subquery_alias;


SELECT ID_sensore, value, timestamp FROM (
    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp,
        'Secondo' AS Aggr
    FROM
        innovacity.umidities
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
        innovacity.umidities1m
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
        innovacity.umidities1o
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
        innovacity.umidities1g
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
        innovacity.umidities1M
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
    value >= ($MinUmidity)
    AND value <= ($MaxUmidity)
    AND (
        timestamp >= $__fromTime
        AND timestamp <= $__toTime
    )
    AND ID_sensore IN ($umd_sensors_id)


     --FOR MAIN DASHBOARD

    SELECT ID_sensore, value, timestamp FROM (
    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp
    FROM
        innovacity.umidities
    WHERE
        cella IN ($Cella)
        AND (
            
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) >= 0
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 300
        )
    GROUP BY timestamp, ID_sensore

    UNION ALL

    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp
    FROM
        innovacity.umidities1m
    WHERE
        cella IN ($Cella)
        AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 300
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 3600
        )
    GROUP BY timestamp, ID_sensore

    UNION ALL

    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp
    FROM
        innovacity.umidities1o
    WHERE
        cella IN ($Cella)
        AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 3600
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 86400
        )
    GROUP BY timestamp, ID_sensore

    UNION ALL

    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp
    FROM
        innovacity.umidities1g
    WHERE
        cella IN ($Cella)
        AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 86400
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 2592000
                )
    GROUP BY timestamp, ID_sensore

    UNION ALL

    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp
    FROM
        innovacity.umidities1M
    WHERE
        cella IN ($Cella)
        AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 2592000
            )
        
    GROUP BY timestamp, ID_sensore
) 
WHERE
 (
        timestamp >= $__fromTime
        AND timestamp <= $__toTime
    )
    AND ID_sensore IN ($umd_sensors_id)