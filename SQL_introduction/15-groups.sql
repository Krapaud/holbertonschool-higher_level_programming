-- Lists the number of records with the same score
-- Displays score and number of occurrences (column named "number")
-- Sorted by number of occurrences in descending order (most frequent to least frequent)
-- GROUP BY groups rows with the same score value
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;