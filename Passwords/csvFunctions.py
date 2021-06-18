import csv

def get_data():
    lst = []
    with open('users.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row)
        file.close()
        return(lst)

def write(lst):
    with open('users.csv','w') as file:
        writer = csv.writer(file)
        for i in lst:
            writer.writerow(i)
        file.close()
