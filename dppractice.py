import sqlite3



connection = sqlite3.connect("sampleDB.db") #connect database
cursor = connection.cursor() #allow interaction with database

# Step 3: Create a table (if it doesn't already exist)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

connection.commit()

# Step 4: Insert data into the table
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Bob', 25))
connection.commit()

cursor.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""") #Program SQl

tables = cursor.fetchall()
print(tables)
cursor.execute("""SELECT name FROM users""")
names = cursor.fetchall()
for name in names:
    print(name[0])

cursor.execute("""SELECT * FROM sampleTable;""")
sampleAll = cursor.fetchall()
print(sampleAll)