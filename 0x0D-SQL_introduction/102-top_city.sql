-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
