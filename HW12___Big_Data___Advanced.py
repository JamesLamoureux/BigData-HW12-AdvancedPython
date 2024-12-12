import sqlite3

# Open the books database
connection = sqlite3.connect("books.db")
cursor = connection.cursor()

# Execute a query to select all data from the titles table in books.db
cursor.execute("SELECT * FROM titles")

# Fetch the column names from the description attribute
column_names = [description[0] for description in cursor.description]

# Fetch all rows from the query result
data = cursor.fetchall()

# Display data in tabular format
# Print the column headers
print(" | ".join(column_names))
print("-" * (len(column_names) * 10))

# Print each row of data
for row in data:
    print(" | ".join(map(str, row)))

# Close the connection
connection.close()

