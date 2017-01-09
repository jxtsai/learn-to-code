# grestest commom measure  between twp integer

a = int(raw_input("enter a number: "))
b = int(raw_input("enter a number: "))

while(a != b):
    if(a > b):
        a = a - b
    else:
        b = b - a

print a 


