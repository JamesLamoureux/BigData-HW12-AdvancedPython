#sqlite3 library is a lightweight disk-based database 
    #that doesn’t require a separate server process.
import sqlite3

# Open the books database
    # Establishes a connection to the 'books.db' SQLite database file.
connection = sqlite3.connect("books.db")

# Creates a cursor object, used to execute SQL commands and 
    # fetch results from the database.
cursor = connection.cursor()

# Execute/create a query to select all data from the titles table in books.db
cursor.execute("SELECT * FROM titles")

# Fetch the column names from the description attribute
    #Extracts the column names from the cursor's 'description' attribute, 
       #where each description tuple's first element contains the column name.
column_names = [description[0] for description in cursor.description]

# Fetch all rows from the query result
    # fetches all rows from the result set of the previously 
       # executed query as a list of tuples.
data = cursor.fetchall()

# Display data in tabular format
# Print the column headers
    # Formats and prints the column names as a single line, 
       # separated by ' | ' for readability.
print(" | ".join(column_names))

#Prints a line of dashes for visual separation, with a 
    #length proportional to the number of columns.
print("-" * (len(column_names) * 10))

# Print each row of data
    # Begins a loop to iterate through each row of the fetched data.
for row in data:
    
    #Formats each row as a string, joining elements with ' | ' for tabular display, 
    #ensuring all data types are converted to strings.
    print(" | ".join(map(str, row)))

# Close the connection
    # Closes the connection to SQLite database to free up 
    # resources/ensure data integrity.    
connection.close()

