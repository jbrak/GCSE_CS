from terminaltables import AsciiTable

boundaries = [["A*",90],["A",80],["B",70],["C",60],["D",50]]

scores = [["Bob",56],["Nora",78],["Rezag",92],["Peter",85], ["Jon",67],["Joe",5]]
grades = [["Name", "Grade"]]

for score in scores:
    for i in boundaries:
        if i[1] <= score[1]:
            grades.append([score[0],i[0]])
            break
    else:
        grades.append([score[0],"fail"])

print(AsciiTable(grades).table)
