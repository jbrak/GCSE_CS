import sqlite3
connection = sqlite3.connect("game.db")

cursor = connection.cursor()

def top10(difficulty):
    cursor.execute("SELECT name, score FROM data WHERE difficulty = '{}' ORDER BY score DESC LIMIT 10".format(difficulty.lower()))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def highscore(name, difficulty):
    cursor.execute("SELECT name, score FROM data WHERE name = '{}' AND difficulty ='{}' ORDER BY score DESC LIMIT 1".format(name.lower(),difficulty.lower()))
    row = cursor.fetchone()

    return row
