import sqlite3
connection = sqlite3.connect("game.db")

cursor = connection.cursor()

def top10():
    cursor.execute("SELECT name, score FROM data ORDER BY score DESC LIMIT 10")
    print("\n Top 10 Scores:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def myRecords(name):
    cursor.execute("SELECT name, score FROM data WHERE name = '{}' ORDER BY score DESC".format(name.lower()))
    rows = cursor.fetchall()

    if bool(rows) == False:
        print("\nInvalid User Name")
    else:
        print("\n {}'s Scores:".format(name))
        for row in rows:
            print(row)
