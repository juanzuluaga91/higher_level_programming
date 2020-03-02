-- Write a script that displays the average temperature (Fahrenheit) 
-- by city ordered by temperature (descending).

SELECT City, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY City DESC
ORDER By avg_temp DESC LIMIT 3;
