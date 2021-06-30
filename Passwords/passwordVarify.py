def password():
    code = input("Enter your password: ")

    score = 0
    upperCase = 0
    lowerCase = 0
    number = 0
    special = 0
    length = 0

    if len(code) >= 8:
        length = 1

    for i in code:
        if (65 <= ord(i)) and (ord(i) <= 90):
            upperCase = 1
        elif (97 <= ord(i)) and (ord(i) <= 122):
            lowerCase = 1
        elif (48 <= ord(i)) and (ord(i) <= 57):
            number = 1
        elif ((32 <= ord(i)) and (ord(i) <= 47)) or ((58 <= ord(i)) and (ord(i) <= 64)) or ((91 <= ord(i)) and (ord(i) <= 96)) or ((123 <= ord(i)) and (ord(i) <= 126)):
            special = 1

    score = upperCase + lowerCase + number + special + length
    if score < 3:
        print("Password Invalid")
        print("Try Again")
        password()
    elif score < 5:
        print("Password could be improved.")
        again = input("Do you want to try again y/n: ")
        if again.lower() == "y":
            password()
    return code

#password()
