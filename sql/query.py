import sqlite3
connection = sqlite3.connect("game.db")

cursor = connection.cursor()

cursor.execute("SELECT name, score FROM data ORDER BY score DESC LIMIT 10")
print("Top 10 Scores:")
rows = cursor.fetchall()
for row in rows:
    print(row)
