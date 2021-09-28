import random
options = ['rock', 'paper', 'scissors']

computer = random.choice(options)

user = input("Enter rock, paper, scissors? ").lower()

if user == computer:
    print('draw')
elif user == 'rock' and computer == 'scissors':
    print("user wins")
elif user == 'scissors' and computer == 'paper':
    print('user wins')
elif user == 'paper' and computer == 'rock':
    print('user wins')
else:
    print('computer wins')
