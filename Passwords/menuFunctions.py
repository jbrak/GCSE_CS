from csvFunctions import get_data, write
from operator import itemgetter
from passwordVarify import password

# Code for adding a new user
def newUser():
    data = get_data()
    #This code cheaks if the username is taken or not
    findUser = itemgetter(0)
    validUser = False

    while validUser == False:
        user = input("\n Enter your new username: ")
        for i in data:
            u = findUser(i)
            if u == user:
                print("\n that username is taken")
                break
        else:
            validUser = True

    code = password()

    #writing the code to the CSV file
    data.append([user,code])
    write(data)
#newUser()


def changePassword():
    data = get_data()
    user = input("enter your username ")
    oldPassword = input("Enter your original password: ")
    code = password()

    for i in data:
        if (i[0] == user) & (i[1] == oldPassword):
            print("Your password has been succsufuly changed.")
            i[1] = password
            write(data)
            break
    else:
        print("Either your username or old password is incorrect. Please try again.")
#changePassword()

#Function to display all the usernames
def displayUsers():
    data = get_data()
    print("\n All Usernames:")
    for i in data:
        print("•", i[0])
#displayUsers()
