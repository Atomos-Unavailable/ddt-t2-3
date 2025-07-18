import sqlite3
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pets (
        species TEXT NOT NULL,
        years INTEGER,
        status TEXT NOT NULL
    )
''')
cursor.execute("INSERT INTO pets (species, years, status) VALUES (?, ?, ?)", ("feline", 10, "dead"))
cursor.execute("INSERT INTO pets (species, years, status) VALUES (?, ?, ?)", ("dog", 23, "alive"))
conn.commit()
cursor.execute("SELECT * FROM pets")
rows = cursor.fetchall()
print("Vetrinary Records:")
for row in rows:
    print(row)

conn.close()