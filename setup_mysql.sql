-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS ef_dev_db;
CREATE USER IF NOT EXISTS 'ef_dev'@'localhost' IDENTIFIED BY 'ef_dev_pwd';
GRANT ALL PRIVILEGES ON `ef_dev_db`.* TO 'ef_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'ef_dev'@'localhost';
FLUSH PRIVILEGES;