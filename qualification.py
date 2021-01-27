from random import choice

qualif = ["KS2","KS3","GCSE", "A Level", "BTEC"]
subject = ["Physics", "Math", "CS", "English", "Art"]
demgra = ["vegans", "teenagers", "parents", "Children", "Grandparents"]
again = "True"

while again == "True":
  print(choice(qualif), choice(subject), "for", choice(demgra))
  again = input("Do you want to go again True or False: ")
