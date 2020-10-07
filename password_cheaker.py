name = input("What is your name:\n")
repeat = True

while repeat == True:
    password = input("Enter your password:\n")
    if len(password) < 8:
            print("Your password is too short.")


    if password == name:
        print("Your password should not be your name")

    repeat = bool(input("do you want to reapeat: True or False\n"))
