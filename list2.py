from random import randint

lst1 = [randint(1,i+10) for i in range(0,9)]
lst2 = [randint(1,i+10) for i in range(0,9)]

print(lst1)
print(lst2)

lst3 = [lst1[i] + lst2[i] for i in range(0,len(lst1))]

print(lst3)

lst3.sort()

print(lst3)
print("Largest:", lst3[-1])
print("Smallest:", lst3[0])
