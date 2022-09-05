name_file = open("names.txt", "a")


# 改用 "with" keyword, 此語法句形則不必使用 close()
with open("student.csv", "r") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in house of {row[1]}.")
        