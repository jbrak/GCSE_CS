import sqlite3
connection = sqlite3.connect("game.db")

cursor = connection.cursor()

def add(name, score):
    sql_command = """INSERT INTO data (id ,name, score)
        VALUES (NULL, "{}",{});""".format(name.lower(),score)
    cursor.execute(sql_command)
    # never forget this, if you want the changes to be saved:
    connection.commit()
    connection.close()
