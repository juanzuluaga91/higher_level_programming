-- Write a script that displays the average temperature (Fahrenheit) 
-- by city ordered by temperature (descending).

SELECT City, AVG(value) AS avg_temp 
FROM temperatures
GROUP BY City 
ORDER by avg_temp DESC;
