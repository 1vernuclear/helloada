import sqlite3

# Connect to the SQLite database (it will create the database.db file if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table (if not exists)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database initialized and table created.")
