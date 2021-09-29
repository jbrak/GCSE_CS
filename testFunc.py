def test(func):
    file = open('testStatements.txt', 'r')
    statements = file.read().splitlines()

    for i in statements:
        try:
            print("when", i , "is entered" ,func(i), 'is returned\n')
        except Exception as e:
            print(e)

def plusOne(num):
    num = float(num)
    num += 1
    return num

test(plusOne)
