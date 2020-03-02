-- Write a script that displays the top 3 of cities temperature 
-- during July and August ordered by temperature (descending)

SELECT City, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY City
ORDER By avg_temp DESC LIMIT 3;
