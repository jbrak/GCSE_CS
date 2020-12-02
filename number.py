num = 0

while num < 10 or num > 20:
    num = int(input("Enter a integer between 10&20:\n"))

    if num > 20:
        print("Too High")
    elif num < 10:
        print("Too Low")

print("Ok")
