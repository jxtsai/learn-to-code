print
def hello():
    print 'Hello!'

def area(width, height):
    return width * height

def print_welcome(nanme):
    print "Welcome,", nanme

name = raw_input("Your name: ")

hello(),
print_welcome(name)
print
print "To find the area of a rectangle."
print "enter the width and heigth below."
print

w = input("Width: ")
while w <= 0:
     print "Must be a positive number"
     w = input("Width: ")

h = input("Height: ")
while h <= 0:
    print "Must be a positive number"
    h = input("Height: ")

print "Width = %d Height = %d so Area = %d" % (w, h, area(w, h))
