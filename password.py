import csvPractice

#csvPractice.write("passwords.csv", ["Username","Password"],[])

what = int(input("""What do you want to do:
1. Create new account
2. Use past account
"""))

match what:
    case 1:
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")
        try:
            float(username)
            print("invalid username. It your username cannot contain only numbers")
            username = input("Enter your Username: ")
        except:
            pass

        while len(password) < 6:
            password = input("Your password is too short, Enter a longer Password: ")

        csvPractice.appen("passwords.csv",[username,password])

    case 2:
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")

        usernames = csvPractice.read("passwords.csv")

        for i in usernames:
            if i[0] == username and i[1] == password:
                print("You are logged in")
                break
        else:
            print("Invalid username or password")
