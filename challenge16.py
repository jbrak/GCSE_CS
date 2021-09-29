try:
    length = float(input("how many hrs do you spend watching TV"))

    if length < 2:
    	print('Thats ok')
    elif length >= 2 and length <= 4:
    	print('That will rot your brain')
    else:
    	print('That is too much TV')
except ValueError:
    print("Invalid statement, write an integer or a float")
