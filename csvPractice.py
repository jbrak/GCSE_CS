import csv
from terminaltables import AsciiTable

def write(cs,header,data):
    f = open(cs, "w")
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
    f.close()

def read(cs):
    f = open(cs,"r")
    reader = csv.reader(f)
    data = []
    for i in reader:
        data.append(i)
    return(data)

def append(cs, data):
    f = open(cs, "a")
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()

write("cs.csv", ["Name","Age"],[["John",1],["James",2]])

append("cs.csv",["Henry",47])

print(AsciiTable(read("cs.csv")).table)
