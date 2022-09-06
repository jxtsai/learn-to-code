import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("new.csv" ,"a") as new_file:
     new_obj = csv.writer(new_file)
     new_obj.writerow(name)