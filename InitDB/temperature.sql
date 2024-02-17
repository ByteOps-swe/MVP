-- Definizione della tabella "temperatures_kafka" per l'input dei dati provenienti da Kafka
CREATE TABLE innovacity.temperatures_kafka (
    timestamp DATETIME64,
    -- Timestamp della rilevazione
    value Float32,
    -- Valore della temperatura
    type String,
    -- Tipo di temperatura (potrebbe essere utile per eventuali distinzioni)
    latitude Float64,
    -- Latitudine della posizione del sensore
    longitude Float64,
    -- Longitudine della posizione del sensore
    ID_sensore String, -- ID del sensore che ha registrato la temperatura
    cella String
) ENGINE = Kafka(
    'kafka:9092',
    'temperature',
    'ch_group_1',
    'JSONEachRow'
);

-- Utilizzo del motore Kafka per leggere i dati
-- Definizione della tabella "temperatures" che conterrà i dati di temperatura consolidati
CREATE TABLE innovacity.temperatures (
    timestamp DATETIME64,
    -- Timestamp della rilevazione
    value Float32,
    -- Valore della temperatura
    type String,
    -- Tipo di temperatura
    latitude Float64,
    -- Latitudine della posizione del sensore
    longitude Float64,
    -- Longitudine della posizione del sensore
    ID_sensore String, -- Nome del sensore
    cella String
) ENGINE = MergeTree() -- Utilizzo del motore MergeTree per l'archiviazione ottimizzata
ORDER BY
    (ID_sensore, timestamp);

-- La scelta di utilizzare il motore MergeTree e l'ordinamento per nome_sensore e timestamp ha diverse ragioni:
-- Efficienza nella lettura dei dati: ClickHouse è progettato per eseguire operazioni analitiche ad alte prestazioni su grandi volumi di dati. L'ordinamento dei dati sulla chiave nome_sensore e timestamp consente al sistema di eseguire interrogazioni di lettura in modo efficiente, specialmente quando si richiedono dati per un determinato sensore o per un intervallo di tempo specifico.
-- Ricerca e filtraggio efficiente: Quando i dati sono ordinati per nome_sensore e timestamp, le query che filtrano i dati per un sensore specifico o per un intervallo di tempo possono eliminare rapidamente le parti dei dati che non sono rilevanti per la query, migliorando notevolmente le prestazioni.
-- Aggregazione e analisi semplificate: L'ordinamento dei dati per timestamp può semplificare l'analisi dei dati temporali, consentendo di eseguire facilmente operazioni di aggregazione e calcoli su finestre temporali specifiche.
-- In sostanza, l'uso del motore MergeTree con l'ordinamento specificato è una scelta strategica per ottimizzare le prestazioni delle query e migliorare l'efficienza complessiva nel processo di archiviazione e interrogazione dei dati delle temperature.
-- Ordinamento dei dati per nome del sensore e timestamp
-- Creazione di una Materialized View per sincronizzare i dati da "temperatures_kafka" a "temperatures"
CREATE MATERIALIZED VIEW temperatureTable_sync TO innovacity.temperatures AS
SELECT
    *
FROM
    innovacity.temperatures_kafka;

-- Creazione della tabella `temperatures1m`
CREATE TABLE innovacity.temperatures1m
(
    ID_sensore String,
    cella String,
    timestamp DATETIME64,
    value Float32, --AggregateFunction(avgState, Float32) CAUSA ALTRI PROBLEMI
   -- PRIMARY KEY (timestamp, ID_sensore, cella) POTREBBE RENDERE IL DATO NON VERITIERO
) ENGINE = MergeTree
ORDER BY (timestamp, ID_sensore, cella);

-- Creazione della Materialized View `temperatures1m_mv`
CREATE MATERIALIZED VIEW innovacity.temperatures1m_mv TO innovacity.temperatures1m AS
SELECT
    toStartOfMinute(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avg(value) AS value
FROM innovacity.temperatures
GROUP BY timestamp, ID_sensore, cella;


-- Creazione della tabella `temperatures1g`
CREATE TABLE innovacity.temperatures1g
(
    ID_sensore String,
    cella String,
    timestamp Date,
    value Float32
) ENGINE = MergeTree
ORDER BY (timestamp, ID_sensore, cella);

-- Creazione della Materialized View `temperatures1g_mv`
CREATE MATERIALIZED VIEW innovacity.temperatures1g_mv TO innovacity.temperatures1g AS
SELECT
    toDate(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avg(value) AS value
FROM innovacity.temperatures
GROUP BY timestamp, ID_sensore, cella;


-- Creazione della tabella `temperatures1M`
CREATE TABLE innovacity.temperatures1M
(
    ID_sensore String,
    cella String,
    timestamp Date,
    value Float32
) ENGINE = MergeTree
ORDER BY (timestamp, ID_sensore, cella);

-- Creazione della Materialized View `temperatures1M_mv`
CREATE MATERIALIZED VIEW innovacity.temperatures1M_mv TO innovacity.temperatures1M AS
SELECT
    toStartOfMonth(timestamp) AS timestamp,
    cella,
    ID_sensore,
    avg(value) AS value
FROM innovacity.temperatures
GROUP BY timestamp, ID_sensore, cella;

