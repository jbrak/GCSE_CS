lst = []
if input("do you want to create a new list: y/n").lower() == "y":
    num = int(input("How Long is the list?: "))
    lst = [input("Enter Item: ").lower() for i in range(0,num)]
else:
    file = open("lst.txt", 'r')
    for i in file:
        lst.append(i[0:-1])
quit = False

while quit == False:
    option = int(input(
    """What do you want to do?:
    1. Reverse list
    2. Slice the list
    3. Print a value
    4. Save to a file
    5. Remove Item
    6. Print the list
    7. Add an Item to the list
    8. Alphabetical
    9. quit
    enter the number you want todo:
    """))

    match option:
        case 1:
            lst2 = []
            for i in range(len(lst)):
                lst2.append(lst[-1])
                lst.remove(lst[-1])
            print(lst2)
            lst = lst2

        case 2:
            max = int(input("What is the max number of the slice: "))
            min = int(input("What is the min number of the slice: "))
            print(lst[min:max])
        case 3:
            print(lst[int(input("Which value do you want to print? Enter the index: "))])

        case 4:
            lst.sort()
            file = open("lst.txt", "w")
            for i in lst:
                file.write(i+"\n")
            file.close()

        case 5:
            lst.remove(input("What item do you want to remove").lower())

        case 6:
            print(lst)

        case 7:
            lst.append(input("Enter New additions: ").lower())

        case 8:
            lst.sort()

        case 9:
            quit = True

        case _:
            print("Invalid option")
