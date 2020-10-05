from random import randint
repeat = "Y"
score = 0

while repeat.upper() == "Y":
    rand_num = randint(0,10)

#    print("\n", rand_num)

    guess = int(input("\nMy Number is between 0-10. Take a Guess\n"))

    while guess != rand_num:
        guess = int(input("Incorrect. Take another guess:\n" ))
        if guess > rand_num:
            print("Your Number is too big ")
        elif guess < rand_num:
            print("Your Number is too low ")

    score += 1
    print("Correct!")
    print("Your score is now", score)
    repeat = input("Do you want to take another go? Y/N\n")
