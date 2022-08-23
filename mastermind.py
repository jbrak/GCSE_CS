strfrom random import randint

colors = ["blue", "green", "red", "pink","orange", "yellow", "black"]

code = [colors[randint(0,7)] for i in range(0,4)]

print(code)

def cheak(code,lst):
    correctPosition = 0
    correctColors = 0
    for i in range(0, 4):
        if code[i] == lst[i]:
            correctPosition += 1
        for j in range(0,4):
            if code[i] == lst[j]:
                correctColors += 1
    return (correctColors, correctPosition)

for i in range(0,12):
    guess = [input("Enter color " + str(i+1) + " ").lower() for i in range(0,4)]

    if guess == code:
        print("You got it right")
        break
    else:
        v = cheak(code,guess)
        print("Correct Colors:", v[0])
        print("Correct colors in correct positions:",v[1])
