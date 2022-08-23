lst = [5,1,2,6]
swap = True

while swap == True:
    swap = False
    for i in range(0,len(lst)-1):
        if lst[i] > lst [i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            swap = True

print(lst)
