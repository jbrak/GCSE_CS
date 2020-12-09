from random import randint
from time import sleep
from card_scoring import score

cards = []
for i in range(1,31):
    if i <= 10:
        cards.append(("red",i))
    elif i <= 20:
        cards.append(("black", i-10))
    else:
        cards.append(("yellow", i-20))

pl1 = []
pl2 = []

for i in range(1,31):
    card = cards.pop(randint(0,len(cards)-1))
    if i % 2 == 0:
        pl2.append(card)

    else:
        pl1.append(card)



score1 = 0
score2 = 0

for i in range(0,len(pl1)):
     s1,s2 = score(pl1[i],pl2[i])
     score1 += s1
     score2 += s2

if s1 > s2:
    print("player 1 wins")
elif s2 > s1:
    print("player 2 wins")
