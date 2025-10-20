-- Computes the average of all scores in second_table
-- AS average renames the result column to "average"
-- AVG() is an aggregation function that calculates the average
SELECT AVG(score) AS average
FROM second_table;