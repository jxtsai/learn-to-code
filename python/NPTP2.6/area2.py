def hello():
    print 'Hello!'

name = raw_input("Your name: ")
hello(),

def print_welcome(nanme):
    print "Welcome,", nanme

print_welcome(name)

def choice():
    print "To find the area of a rectangle, square, or cirlce."
    print "1. rectangle"
    print "2. square"
    print "3. circle"

choice = raw_input("Your choice? ")


def area_rectangle(w, h):
    return w * h

def area_square(w):
    return w * w

def are_cirlce(r):
    return 3.14 * r **2

if choice == "1":
    w = input("Width: ")
    h = input("Height: ") 
    print "The area of the rectangle is ", area_rectangle(w, h)
elif choice == "2":
    w = input("width: ") 
    print "The area of the square is ",area_square(w)
elif choice == "3":
    r = input("Radius: ")
    print "The area of the circle is ", are_cirlce(r)
else:
    print "Unrecognized option."
