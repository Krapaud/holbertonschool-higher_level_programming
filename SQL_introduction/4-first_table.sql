-- Creates a table first_table in the current database
-- Columns: id (INT) and name (VARCHAR(256))
-- IF NOT EXISTS prevents an error if the table already exists
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
