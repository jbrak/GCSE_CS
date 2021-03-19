import sqlite3
connection = sqlite3.connect("game.db")

cursor = connection.cursor()

sql_command = """
CREATE TABLE data (
id INTEGER PRIMARY KEY,
name VARCHAR(10),
score INTEGER,
difficulty CHAR(1));"""

cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()
