word = "pizza"
guess = input("Enter Your First Guess: ")

for j in range(1,6):

    if

    if guess == word:
        print("You got it, its", word)
        break

    for i in guess:
        #print(i, word.count(i))
        if word.count(i) != 0:
            if guess.index(i) == word.index(i):
                print(i,"Right Letter, Right Place")
            else:
                print(i,"Right Letter, Wrong Place")
    guess = input("Enter Your next Guess: ")
