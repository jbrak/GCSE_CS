import sqlite3
connection = sqlite3.connect("game.db")

cursor = connection.cursor()

name = input("Enter your Name/Username: ")
score = int(input("Enter you Score: "))

sql_command = """INSERT INTO data (id ,name, score)
    VALUES (NULL, "{}",{});""".format(name,score)

cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()
