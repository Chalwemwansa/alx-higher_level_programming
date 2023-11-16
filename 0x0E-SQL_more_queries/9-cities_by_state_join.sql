-- script that lists all the cities in the database passed as an argument
-- uses only one select statement
SELECT c.id AS id, c.name AS name, s.name AS name
	FROM states s, cities c
	WHERE s.id = c.state_id;
