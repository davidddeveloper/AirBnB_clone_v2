-- prepares a MySQL server for the project

-- creates the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creates user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY '#1Hbnb_test_pwd';

-- grants privilidges
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
