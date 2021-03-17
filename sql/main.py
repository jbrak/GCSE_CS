import sqlite3
from query import top10, myRecords
from addData import add

connection = sqlite3.connect("game.db")
cursor = connection.cursor()

name = input("Enter your name: ")

while True:
    print("What do you want to do?")
    print('''
    Press 1 to add a new game record
    Press 2 to show the leaderboard
    Press 3 to show your records
    Press 4 to quit
    ''')
    num = input()

    if num == '1':
        add(name,input("Enter your score: "))
    elif num == '2':
        top10()
    elif num == '3':
        myRecords(name)
    elif num == "4":
        break
    else:
        print("Invald Number")
