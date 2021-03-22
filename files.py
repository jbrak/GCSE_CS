f = open("scores.txt", 'a')

score = input("enter a score:\n")

f.write("\n"+score)
f.close()

f = open("scores.txt","r")
lst = []
for i in f:
    lst.append(int(i))

lst.sort(reverse=True)
print(lst[:10])
