-- Lists all records where the name field is not NULL
-- Displays score and name, sorted by score in descending order
-- IS NOT NULL filters rows with a non-null value for name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;