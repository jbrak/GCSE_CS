from math import floor
lst = [9,7,3,4,1,2,86,4,5,2,9]
target = 86

lst.sort()
match = False

while match == False:
    midpoint = floor(len(lst)/2)

    if lst[midpoint] == target:
        match = True
        print("match found ", lst[midpoint], 'at index', midpoint)

    elif lst[midpoint] > target:
        lst = lst[0:midpoint]

    elif lst[midpoint] < target:
        lst = lst[midpoint:len(lst)]
