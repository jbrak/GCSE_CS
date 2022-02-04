from random import randint,choice
name = input("Enter your name: ")
score = 0

def question():
    num1 = randint(1,20)
    num2 = randint(1,20)
    symbol = choice(["+","-","/","*"])

    awnser = int(input(str(num1)+symbol+str(num2)+"=\n"))

    if symbol == "+":
        correct = num1+num2
    elif symbol == "-":
        correct = num1- num2
    elif symbol == "/":
        correct = num1 / num2
    else:
        correct = num1 * num2

    if awnser == correct:
        print("correct awnser")
        return 1
    else:
        print("Wrong its actually", correct)
        return 0


for i in range(1,10):
	score += question()

print(name,"got",score,"/10")

file = open("file.txt", "r")

scores = []
for i in file:
    scores.append(i)
    index = i.index(',')
    if i[:index] == name:
        tScore = int(i[index+1:]) + score
        index2 = scores.index(i)

file.close()
file = open("file.txt","w")

try:
    scores[index2] = (name + ',' + str(tScore))
except:
    scores.append(name + ',' + str(score))

print(scores)
for i in scores:
    file.write(i)
