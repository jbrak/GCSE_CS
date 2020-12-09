order = input("Do you want to sort it in Asending or Decending Order? a/d ").lower()
amount = int(input("How many values do you want to enter "))

lst = [int(input("Enter number " + str(i + 1) + " ")) for i in range(0, amount)]

if order == "a":
    lst.sort()
elif order == "d":
    lst.sort(reverse=True)
else:
    print("That was not an a or d")
print(lst)
