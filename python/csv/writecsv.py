import csv

with open('test.csv', 'w') as csv_file:
    test_writer = csv.writer(csv_file, delimiter=",")
    test_writer.writerow(["name", "age", "school", "gender"])
    test_writer.writerow(["David", "23", "NTU", "Male"])
    test_writer.writerow(["Diana", "38", "Royal Nurse", "Female"])