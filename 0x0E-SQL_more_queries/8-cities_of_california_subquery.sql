-- list all the cities that can be found in the table using a foreign key
-- use of nested querries demonstrated here
SELECT id, name FROM cities
	WHERE state_id = (
		SELECT id FROM states
		WHERE name = 'California')
	ORDER BY cities.id;
