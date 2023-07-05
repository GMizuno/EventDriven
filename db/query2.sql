SELECT "coinId",
       DATE_TRUNC('hour', TO_TIMESTAMP(event_time, 'YYYY-MM-DD HH24:MI:SS')) AS hour_bucket,
       MIN(price) AS min_price,
       MAX(price) AS max_price,
       AVG(price) AS avg_price
FROM coin_price
GROUP BY "coinId", hour_bucket
ORDER BY "coinId", hour_bucket;