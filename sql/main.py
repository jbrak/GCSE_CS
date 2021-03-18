import sqlite3
from random import randint
from query import top10, highscore
from addData import add

connection = sqlite3.connect("game.db")
cursor = connection.cursor()

name = input("Enter your name: ")
score = 150
rand_num = randint(0,10)
guess = int(input("\nMy Number is between 0-10. Take a Guess\n"))

while guess != rand_num:
    score -= randint(5,20)
    guess = int(input("Incorrect. Take another guess:\n" ))
    if guess > rand_num:
        print("Your Number is too big ")
    elif guess < rand_num:
        print("Your Number is too low ")

print("Correct!")
print("Your score is", score)

highscore = highscore(name)
add(name,score)

if bool(highscore) == False:
    "nothing"
elif score > highscore[-1]:
    print("You beat your highscore of", highscore[-1])
else:
    print("You have not beaten your highscore of", highscore[-1],'yet.')
    print()
print("This is the leaderboard:\n")
top10()
