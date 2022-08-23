s = int(input("enter the distance of the jorney: "))
passengers = int(input("enter the number of passengers: "))

cost_s = 3+((s-1)*2)

if passengers > 4:
    cost_s *= 1.5

print(cost_s)
