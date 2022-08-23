amount = int(input("How many nums? "))

num = [int(input("enter num: ")) for i in range(0,amount)]

smallest = num[0]
largest = num[0]

for i in num:
    if i < smallest:
        smallest = i
    elif i > largest:
        largest = i

sort = [num.pop(num.index(smallest)), num.pop(num.index(largest))]

print(sort)

for i in num:
    for j in range(0,len(sort)-1):
        if (sort[j] <= i) and (sort[j+1] >= i):
            sort.insert(j+1,i)
            break

print(sort)
print(num)
