
#import file
import csv
#puts all possiable wordsd in list
with open("valid_solutions.csv") as r:
    words = []
    for i in csv.reader(r):
        words.append(i[0])

amountOfLetters = int(input("How many letters do you know? "))
#list of the letters they know
letters = []
for i in range(0,amountOfLetters):
    letter = input("Enter the letter ")
    position = int(input("Enter the position of the letter, if you do not know the position put 6: "))
    letters.append([letter, position])

possibleWords = []
#looks through possible words and compares them to the letter you input
for j in letters:
    lst = []
    for i in words:
        if (j[0] in i) == True:
            lst.append(i)
    possibleWords = possibleWords + lst

possibleWords1 = []
#gets rid of duplicates
for i in possibleWords:
    if possibleWords.count(i) > (len(letters)-1) and possibleWords1.count(i) == 0:
        possibleWords1.append(i)

possibleWords2 = []
for j in letters:
    lst = []
    for i in possibleWords1:
        if j[1] == 6:
            lst.append(i)
        elif j[0] == i[j[1]-1]:
            lst.append(i)
    possibleWords2 = possibleWords2 + lst

possibleWords3 = []

for i in possibleWords2:
    if possibleWords2.count(i) > (len(letters)-1) and possibleWords3.count(i) == 0:
        possibleWords3.append(i)

#asking if you know any letters that arent in the word
noletters = input('do you know any letters that arent in the word')
if noletters == 'no':
    print(possibleWords3)
elif noletters == 'yes':
#it will then ask how many letters you know to then ask to enter a letter that amount of times
    amountOfLetter = int(input("How many letters do you know? "))
#it will then ask you what the letter is the amount of times you put in
    letterss = []
    for i in range(0,amountOfLetter):
        lettersss = input("Enter the letter ")
        letterss.append(lettersss)
#it goes through all the possible solutions and matchs them to the letter you input
    possibleWordss = []
    for j in letterss:
        lst = []
        for i in possibleWords3:
            if (j[0] not in i) == True:
                lst.append(i)
        possibleWordss = possibleWordss + lst


    possibleWords11 = []
#gets rid of duplicates
    for i in possibleWordss:
        if possibleWordss.count(i) > (len(letterss)-1) and possibleWords11.count(i) == 0:
            possibleWords11.append(i)

    print(possibleWords11)
else:
    print(possibleWords3)
