import csv

with open("test.csv", "r") as file:
    #
    csv_file = csv.reader(file, delimiter=",")
    for row in csv_file:
        print(row)    

with open("test.csv", "r") as file:
    content = file.readlines()
    for line in content:
        print(line)    