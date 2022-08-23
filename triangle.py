sides = [float(input("Enter Side Length: ")) for i in range(0,3)]

if (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[1] != sides[2]):
    print("Not scalene")
elif sides[0] == sides[1] == sides[2]:
    print("Equilateral")
else:
    print("isosolease")
