from random import randint
from datetime import datetime

name = input("Enter your surname: ")
age = int(input("Enter your age: "))
now = datetime.now()

password = ""
letters = [name[randint(0, len(name) - 1)] for i in range(0, 3)]

password += str(now.strftime("%M")) + letters[0] + str(age) + str(now.strftime("%S")) + "-" +letters[1] + str(now.strftime("%S")) + str(now.strftime("%Y"))

print(password)