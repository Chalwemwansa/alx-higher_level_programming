-- script that creates a table and does not fail if the table exists
-- the tavle name to be created is id_not_null in the database passed as argument to mysql
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1, name VARCHAR(256));
