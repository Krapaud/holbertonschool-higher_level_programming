# SQL Introduction

This directory contains SQL scripts for learning MySQL basics.

## Files

- `0-list_databases.sql` - List all databases
- `1-create_database_if_missing.sql` - Create database hbtn_0c_0
- `2-remove_database.sql` - Delete database hbtn_0c_0
- `3-list_tables.sql` - List all tables in a database
- `4-first_table.sql` - Create first_table
- `5-full_table.sql` - Show full table description
- `6-list_values.sql` - List all rows from first_table
- `7-insert_value.sql` - Insert a row into first_table
- `8-count_89.sql` - Count records with id = 89
- `9-full_creation.sql` - Create and populate second_table
- `10-top_score.sql` - List records ordered by score
- `11-best_score.sql` - List records with score >= 10
- `12-no_cheating.sql` - Update Bob's score
- `13-change_class.sql` - Delete records with score <= 5
- `14-average.sql` - Compute average score
- `15-groups.sql` - Count records by score
- `16-no_link.sql` - List records with non-null names

## Usage

Run scripts with:
```bash
cat <script_name>.sql | mysql -hlocalhost -uroot -p [database_name]
```
