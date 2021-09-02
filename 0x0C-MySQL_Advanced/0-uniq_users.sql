-- create table 'users' with attributes id, email, name
CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
email VARCHAR(255) UNIQUE NOT NULL,
name VARCHAR(255)
)
