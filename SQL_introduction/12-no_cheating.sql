-- Updates Bob's score to 10 in the table second_table
-- Uses the name field to identify the record (not the id)
UPDATE second_table
SET score = 10
WHERE name = "Bob";
