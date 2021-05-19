from menuFunctions import newUser, changePassword, displayUsers

switcher = {
    1 : "newUser()",
    2 : "changePassword()",
    3 : "displayUsers()",
    4 : "cont = 0"
}

cont = 1

while cont == 1:
    try:
        menu = int(input('''
        1 : Create new User ID
        2 : Change a password
        3 : Display all User IDs
        4 : Quit

        Enter selection:
        '''))
        exec(switcher[menu])
    except:
        print("Invalid menu choice entered")

print("\ns¡Goodbye! 👋")
