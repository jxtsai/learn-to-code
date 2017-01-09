def shout(string):
    for character in string:
        print "Gimme a " + character
        print "'%s'" %character

shout("Lose")

def middle(string):
    print "The middle character is: ", string[len(string)/2]

middle("abcdefg")
middle("The Python Programming Language")
middle("Atlanta")

def to_upper(string):
    upper_case = ""
    for character in string:
        if 'a' <= character <= 'z':
            location = ord(character) - ord('a')
            new_ascii = location + ord('A')
            character = chr(new_ascii)
        upper_case = upper_case  + character
    return upper_case

print to_upper("This is Text")

def to_string(in_int):
    out_str = ""
    prefix = ""
    if in_int < 0:
        prefix = "-"
        in_int = -in_int
    while in_int / 10 != 0:
        out_str = chr(ord('0') + in_int % 10) + out_str
        in_int = in_int / 10
    out_str = chr(ord('0') + in_int % 10) + out_str
    return prefix + out_str

def to_int(in_str):
    out_num = 0
    if in_str[0] == "-":
        multiplier = -1
        in_str = in_str[1:]
    else:
        multiplier = 1
    for x in range(0, len(in_str)):
        out_num = out_num * 10 + ord(in_str[x]) -ord('0')
    return out_num * multiplier

print to_string(2)
print to_string(23456)
print to_string(-232334)
print to_int("12243")
print to_int("-322")
























