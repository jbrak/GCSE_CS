lst = [5,3,2,7]

print(lst)

while True:
    sorted = 0
    for i in range(0,len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            sorted += 1
    if sorted == 0:
        break

print(lst)
