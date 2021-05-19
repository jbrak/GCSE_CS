from csvFunctions import get_data, write
from operator import itemgetter

# Code for adding a new user
def newUser(data = get_data()):
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

    password = input("\n Set your password: ")
    #Add Password Validation Code Here

    #writing the code to the CSV file
    data.append([user,password])
    write(data)
newUser()


#def changePassword(data = get_data()):

#Function to display all the usernames
def displayUsers(data = get_data()):
    print("\n All Usernames:")
    for i in data:
        print("•", i[0])
displayUsers()
