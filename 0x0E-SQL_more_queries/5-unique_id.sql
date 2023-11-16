-- script that creates a table and does not fail if the table exists
-- the tavle name to be created is unique_id in the database passed as argument to mysql
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
