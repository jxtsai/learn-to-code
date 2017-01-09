print "Welcome to the average calculator, please insert a number"
currentaverage = 0
numofnums = 0
while True:
	newnumber = int(raw_input("New number: "))
	numofnums += 1
	currentaverage = (round((((currentaverage*(numofnums-1) + newnumber)/numofnums), 3))
	print "The current average is", str(round(currentaverage, 3))
