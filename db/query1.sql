SELECT "coinId", min(price), max(price), avg(price)
FROM coin_price
WHERE TO_TIMESTAMP(event_time, 'YYYY-MM-DD HH24:MI:SS') >= NOW() - INTERVAL '10 minutes'
GROUP BY "coinId"