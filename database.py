import sqlite3

# Connect to the database
connection = sqlite3.connect("finance.db")

# Create a  cursor
cursor = connection.cursor()

# Create the expenses table
cursor.execute("""
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    amount REAL,
    category TEXT
)
""")

# Save changes and close the connection
connection.commit()
connection.close()

print("Expenses table created successfully in the database!")
