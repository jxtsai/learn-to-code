go = 'y'
x = 0

def hello():
	print "Hello"

def bye():
	print "Bye"

def hola():
	print "Hola is Spanish for Hello"

def adios():
	print "adios is Spanish for bye"

menu = [hello, bye, hola, adios]

while x < len(menu):
	print "function", menu[x].__name__, "press", "["+str(x)+"]"
	x += 1

while go != "n":
	c = int(raw_input("Select Fucntion: "))
	menu[c]()
	go = raw_input("Try again? [y/n]: ")

print "\nBye!"

