lst = [9,7,3,4,1,2,86,4,5,2,9]
target = 86


for i in lst:
    if i == target:
        print("found",target," at index:", lst.index(i))
