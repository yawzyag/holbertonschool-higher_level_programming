-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name = 'California');
