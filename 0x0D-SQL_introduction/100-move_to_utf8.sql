-- converts a databasse, table and column to utf8mb4 and collate
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE hbtn_0c_0;

ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256)
COLLATE utf8mb4_unicode_ci;
