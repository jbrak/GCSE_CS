import sqlite3
from random import randint
from query import top10, highscore
from addData import add

connection = sqlite3.connect("game.db")
cursor = connection.cursor()

name = input("Enter your name: ")
difficulty = input("Hard, Medium or Easy Difficulty? h/m/e\n").lower()

score = 150

if difficulty == "e":
    rand_num = randint(0,10)
    guess = int(input("\nMy Number is between 0-10. Take a Guess\n"))
elif difficulty == "m":
    rand_num = randint(0,35)
    guess = int(input("\nMy Number is between 0-35. Take a Guess\n"))
elif difficulty == "h":
    rand_num = randint(0,100)
    guess = int(input("\nMy Number is between 0-100. Take a Guess\n"))
else:
    print("invalid difficulty")
    exit()

while guess != rand_num:
    score -= randint(5,20)
    guess = int(input("Incorrect. Take another guess:\n" ))
    if guess > rand_num:
        print("Your Number is too big ")
    elif guess < rand_num:
        print("Your Number is too low ")

print("Correct!")
print("Your score is", score)

highscore = highscore(name, difficulty)
add(name,score,difficulty)

if bool(highscore) == False:
    "nothing"
elif score > highscore[-1]:
    print("You beat your highscore of", highscore[-1], "on difficulty", difficulty)
else:
    print("You have not beaten your highscore of", highscore[-1],'yet.')
    
print("\nThis is the leaderboard for",difficulty,"difficulty:\n")
top10(difficulty)
