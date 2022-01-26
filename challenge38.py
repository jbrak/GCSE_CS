
saved = int(input("Enter amount saved: "))
years = int(input("Enter the number of years: "))

money = 0

print("Year | Start | Paid in | Interest | Final")

for i in range(1,years+1):
	interest = (money+saved)*0.1
	print(i,"|",round(money),"|",round(saved),"|",round(interest),"|",round(money+interest+saved))
	money+= saved + interest
