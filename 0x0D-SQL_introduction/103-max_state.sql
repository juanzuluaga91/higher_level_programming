-- Write a script that displays the max temperature 
-- of each state (ordered by State name).

SELECT state, max(value) AS max_temp 
FROM temperatures 
GROUP by state
ORDER By  state ASC LIMIT 3;
