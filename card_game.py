from random import randint
from time import sleep
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
        print("Player 2 draws")
        pl2.append(card)
        sleep(0)

    else:
        print("Player 1 draws")
        pl1.append(card)
        sleep(1)

print(pl1, pl2)

print(pl1[3].count("yellow"))
