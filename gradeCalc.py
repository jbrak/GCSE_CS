def gradeCalculator(grade):
    if grade >= 90:
        return "A*"
    elif grade >= 80:
        return "A"
    elif grade >= 70:
        return "B"
    elif grade >= 60:
        return "C"
    else:
        return "Fail"

print(gradeCalculator(int(input("Enter a Grade: "))))
