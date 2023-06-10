import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('sip_data.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sip_packets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        destination TEXT,
        call_id TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

