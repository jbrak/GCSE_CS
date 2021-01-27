from random import choice

game = ["r"]*10 + ["p"] + ["s"]
computerScore = 0
playerScore = 0

for i in range(0,10):
  player = input("Rock, Paper or Sissors. r/p/s: ").lower()
  computer = choice(game)

  if player == "r" and computer == "s":
    playerScore += 1
    print("Player Wins")
  elif player == "s" and computer == "p":
    playerScore += 1
    print("Player Wins")
  elif player == "p" and computer == "r":
    playerScore += 1
    print("Player Wins")
  elif player == computer:
    print("Draw")
  else:
    computerScore += 1
    print("Computer Wins")

  print(computer)

print("Player: ", pl
