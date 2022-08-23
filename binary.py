binaryNum = "01111110"
decimalNum = 0

for i in range(0,8):
    binaryDigit = int(binaryNum[i])

    decimalNum += binaryDigit * (2**(7-i))

print(decimalNum)
