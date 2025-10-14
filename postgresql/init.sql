-- Create a user and grant privileges
CREATE USER abojaber WITH PASSWORD 'qwe123';

-- Create a database and grant all privileges to the user
CREATE DATABASE mydatabase OWNER myuser;

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;

-- Create a table
CREATE TABLE mytable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

-- Insert some sample data into the table
INSERT INTO mytable (name, email)
VALUES 
    ('Abojaber', 'abojaber@abojaber.com'),
    ('Jane Smith', 'jane.smith@example.com'),
    ('Bob Johnson', 'bob.johnson@example.com');
