lst1 = [1,2,3,4,5,6]
lst2 = [1,2,3,4,5,6]

lst3 = [lst1[i] + lst2[i] for i in range(0,len(lst1))]
lst3.sort()

print("Largest:", lst3[-1])
print("Smallest:", lst3[0])
