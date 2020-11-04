count = int(input("How Many names do you want to enter? "))
lst = []
rev = []

for i in range(0,count):
    lst.append(input("Name " + str(i+1) + " : "))

if input("Do you want to reverse the list? Y/N ").upper() == "Y":
    for i in range(0,count):
        rev.append(lst.pop(-1))
    print(rev)
else:
    print(lst)
