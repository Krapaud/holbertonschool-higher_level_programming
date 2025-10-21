-- Creates the table unique_id on your MySQL server
CREATE TABLE IF NOT EXISTS first_table (
    id INT DEFAULT unique_id 1,
    name VARCHAR(256)
);
