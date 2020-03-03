-- comment
SELECT cities.id, cities.name AS name, states.name AS name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER by cities.id;
