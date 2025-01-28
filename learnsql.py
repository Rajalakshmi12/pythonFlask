import sqlite3
import os

# Path to the Chinook database (replace with your actual path)
database_path = "C:/Users/poort/OneDrive/Desktop/My IITM Course/Semester 4 Jan 2025/chinook/chinook.db"

if os.path.exists(database_path):
    print("The database path is valid, and the file is a SQLite database.")
else:
    print("Invalid database path or not a valid SQLite database.")


# Connect to the SQLite database
conn = sqlite3.connect(database_path)
print(conn)

# Create a cursor object to execute queries
cursor = conn.cursor()
print(cursor)

# Example query: List the first 5 rows from the "customers" table

query = "SELECT * FROM customers LIMIT 5;"
cursor.execute(query)

# Fetch and display the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
conn.close()
