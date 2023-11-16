-- create_user_script.sql

DELIMITER //

CREATE PROCEDURE CreateUserIfNotExists()
BEGIN
    DECLARE num_users INT;
    SELECT COUNT(*) INTO num_users FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';

    IF num_users = 0 THEN
        SET @sql_query = (CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd');
        PREPARE stmt FROM @sql_query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

        SELECT 'User created successfully' AS result;
    ELSE
        SELECT 'User already exists. Skipping creation.' AS result;
    END IF;
END //

DELIMITER ;

