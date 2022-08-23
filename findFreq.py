import string

word = "A House has a Roof"
alphabet = []

for i in string.ascii_lowercase:
    alphabet.append([i])

letter = 0
for i in word:
    alphabet[letter].append(word.count(i))
    letter +=1

print(alphabet)
