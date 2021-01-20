num = input("Enter a number: ")

for i in num:
    if i == ".":
        try:
            num = float(num)
            print("Your number is a float.")
        except ValueError:
            print("That is not a number")
        break


if type(num) != float:
    try:
        num = int(num)
        print("Your number is an integer")
    except ValueError:
        print("Thats not a number")

