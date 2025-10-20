-- Lists records with a score greater than or equal to 10
-- Displays score and name, sorted by score in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
