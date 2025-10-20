-- List all records where name is not null
-- Display score and name, ordered by score (descending)
-- Use WHERE with IS NOT NULL or similar condition
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;