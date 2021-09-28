def calc(age = int):
    if age <= 2:
        return age*12
    elif age > 2:
        return 48 + ((age - 2)*6)

dog = int(input('enter the age of the dog: '))

calc(dog)
