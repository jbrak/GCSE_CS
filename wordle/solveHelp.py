import csv

with open("valid_solutions.csv") as r:
    words = []
    for i in csv.reader(r):
        words.append(i[0])

amountOfLetters = int(input("How many letters do you know? "))

letters = []
for i in range(0,amountOfLetters):
    letter = input("Enter the letter ")
    position = int(input("Enter the position of the letter, if you do not know the position put 6: "))
    letters.append([letter, position])

possibleWords = []

for j in letters:
    lst = []
    for i in words:
        if (j[0] in i) == True:
            lst.append(i)
    possibleWords.append(lst)

possibleWords1 = []

for i in possibleWords[0]:
    if possibleWords[1].count(i) > 0:
        possibleWords1.append(i)

possibleWords2 = []
for j in letters:
    lst = []
    for i in possibleWords1:
        if j[1] == 6:
            lst.append(i)
        elif j[0] == i[j[1]-1]:
            lst.append(i)
    possibleWords2.append(lst)


possibleWords3 = []

for i in possibleWords2[0]:
    if possibleWords2[1].count(i) > 0:
        possibleWords3.append(i)

print(possibleWords3)
