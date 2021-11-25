from math import floor

lstOriginal = [9,7,3,4,1,2,86,4,5,2,9]
lst = sorted(lstOriginal)
target = 86

print(lst)

found = int()

while found != target:
    midpoint = floor((len(lst))/2)
    print(midpoint)
    found = lst[midpoint]

    if target < found:
        lst = lst[0:midpoint]
        print(lst)
    elif target > found:
        lst = lst[midpoint:len(lst)]
        print(lst)

print(lstOriginal)
print("Found", target, "at index", lstOriginal.index(target))
