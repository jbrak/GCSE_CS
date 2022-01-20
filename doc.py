registered = input("Are you registered? True/False ")

if registered == "False":
    print("You are now registered")
elif input("Are your details up to date? True/False") == 'False':
    print("You are now upto date")

from random import choice
from time import sleep

dr = False

while not(dr):
    dr = choice([True, False])

    if dr:
        print("You can see the doctor")
    else:
        print("waiting")
        sleep(50)
