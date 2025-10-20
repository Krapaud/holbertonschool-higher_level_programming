-- Creates the table second_table with three columns: id, name, score
-- Then inserts 4 initial records
-- John (id=1, score=10), Alex (id=2, score=3), Bob (id=3, score=14), George (id=4, score=8)
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score)
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
