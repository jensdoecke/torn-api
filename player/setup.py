import sqlite3
conn = sqlite3.connect('torn-users.db')
c = conn.cursor()
c.execute("""CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    state TEXT,
    age INTEGER,
    role TEXT,
    created DATETIME,
    last_action DATETIME,
    total_duration INTEGER,
    total_units TEXT,
    rank TEXT,
    level INTEGER,
    last_update DATETIME
)""")
conn.commit()
conn.close()