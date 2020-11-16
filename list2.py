lst1 = [int(input("enter a number: ")) for i in range(0,9)]
lst2 = [int(input("enter a number: ")) for i in range(0,9)]

lst3 = [lst1[i] + lst2[i] for i in range(0,len(lst1))]

print(lst3)

lst3.sort()

print(lst3)
print("Largest:", lst3[-1])
print("Smallest:", lst3[0])
