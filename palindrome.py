word = input("Enter a word: ").lower()

for i in range(0,len(word)):
    if word[i] == word[-i-1]:
        palindrome = True
    else:
        palindrome = False
        break

print("Palindrome Statas: ",palindrome)
