-- script that creates a table in the mysql database
-- the database name is passed as an argument to mysql
CREATE TABLE IF NOT EXISTS force_name(
	id INT, name VARCHAR(256) NOT NULL);
