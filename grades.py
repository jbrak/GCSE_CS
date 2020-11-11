try:
    score = int(input("What is your score: "))
except ValueError:
    score = int(input("Your score should be a number\nEnter your score: "))

if score < 50:
    print("Fail")
elif score < 70:
    print("Pass")
elif score < 90:
    print("Merit")
else:
    print("Distinction")
