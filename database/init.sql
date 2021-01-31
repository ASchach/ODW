DROP DATABASE IF EXISTS db;
CREATE DATABASE db;
USE db;
CREATE TABLE IF NOT EXISTS persons (
    PersonID int(10) AUTO_INCREMENT PRIMARY KEY, 
    Firstname VARCHAR(20), 
    Lastname VARCHAR(20)
    );
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON *.* TO 'admin'@'localhost';
CREATE USER 'admin'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';
FLUSH PRIVILEGES;