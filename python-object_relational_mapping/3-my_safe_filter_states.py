#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments from command line (including state name)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query using parameterized query (safe from injection)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))
    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()

