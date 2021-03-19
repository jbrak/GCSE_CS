import sqlite3
connection = sqlite3.connect("game.db")

cursor = connection.cursor()

def add(name, score, difficulty):
    sql_command = """INSERT INTO data (id ,name, score, difficulty)
        VALUES (NULL, "{}",{},'{}');""".format(name.lower(),score, difficulty.lower())
    cursor.execute(sql_command)

    connection.commit()
    connection.close()
