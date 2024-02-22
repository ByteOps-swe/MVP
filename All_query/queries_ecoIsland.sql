SELECT ID_sensore, value, timestamp FROM (
    SELECT
        ID_sensore AS ID_sensore,
        avgMerge(value) AS value,
        timestamp AS timestamp
    FROM
        innovacity.ecoIslands
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
        innovacity.ecoIslands1m
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
        innovacity.ecoIslands1o
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
        innovacity.ecoIslands1g
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
        innovacity.ecoIslands1M
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
    AND ID_sensore IN ($ecoIs_sensors_id)