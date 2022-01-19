statement = "When Mr. Bilbo Baggins of Bag End announced"
letter1position = statement.count("a")
letter2position = statement.count("e")
letter3position = statement.count("i")
letter4position = statement.count("o")
letter1 = statement[letter1position-1:letter1position]
letter2 = statement[letter2position-1:letter2position]
letter3 = statement[letter3position-1:letter3position]
letter4 = statement[letter4position-1:letter4position]
password = letter4 + letter2 + letter3 + letter1
print(letter1, letter2, letter3, letter4)
print(letter2position)
print(password)
