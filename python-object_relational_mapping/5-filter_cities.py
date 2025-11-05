#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state
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

    # Execute SQL query with JOIN and WHERE (SQL injection free)
    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    cursor.execute(query, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Display results as comma-separated list
    print(", ".join([row[0] for row in results]))

    # Close cursor and connection
    cursor.close()
    db.close()
