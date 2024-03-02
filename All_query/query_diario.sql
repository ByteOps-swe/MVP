SELECT 
    ID_sensore,
    avg(value) AS value,
    CASE
        WHEN (
            'Secondo' = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) >= 0
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 300
                )
            )
        ) THEN toStartOfSecond(timestamp)
        WHEN (
            'Minuto' = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 300
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 3600
                )
            )
        )  THEN toStartOfMinute(timestamp)
        WHEN (
            'Ora' = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 3600
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 86400
                )
            )
        ) THEN toStartOfHour(timestamp)
        WHEN (
            'Giorno' = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 86400
                    AND (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) <= 2592000
                )
            )
        ) THEN toDate(timestamp)
         WHEN (
            'Mese' = '${AggregazioneTemporale}'
            OR (
                '${AggregazioneTemporale}' = 'Automatico'
                AND (
                    (toUnixTimestamp($__toTime) - toUnixTimestamp($__fromTime)) > 2592000
                )
            )
        ) THEN toStartOfMonth(timestamp)
        ELSE timestamp
    END AS timestamp
FROM innovacity.$tabella
WHERE
 cella IN ($Cella) 
    AND $__timeFilter(timestamp)
    AND ID_sensore IN ($sensors_id)
GROUP BY ID_sensore,timestamp
HAVING
  value >= ($Min)
    AND value <= ($Max)
