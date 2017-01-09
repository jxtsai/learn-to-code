

i = 0
for i in range(1, 4):
    name = raw_input("what is your name? ")
    password = raw_input("what is the password? ")
    r = 3 - i
    if name == "Josh" and password == "Friday":
        print "Welcome Josh"
        break
    elif name == "Fred" and password == "Rock":
        print "Weclome Fred"
        break
    else:
        print "Wrong, this is your #%d guess, you have %d more guess" %(i, r)
    i += 1


