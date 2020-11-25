lst = [5,6,3,8,10]
print(lst)

for i in range(0,len(lst)):
    index = i
    print(i)
    while index > 0 and lst[index-1] > lst[index]:
        lst[index],lst[index-1] = lst[index-1], lst[index]
        index -= 1

print(lst)
