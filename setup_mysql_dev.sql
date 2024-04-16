-- prepares a MySQL server for the project

-- creates the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creates user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'

-- rants privilidges
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev
GRANT SELECT ON performance_schema.* TO hbnb_dev