-- List number of records with same score
-- Display score and count (as 'number')
-- Sort by count (descending)
-- Use GROUP BY and COUNT
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;