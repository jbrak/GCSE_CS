lst = [9,7,3,4,1,2,86,4,5,2,7]
target = 86

for i in range(0,len(lst)):
    if lst[i] == target:
        print("Target found at list index: ", i)
        break
