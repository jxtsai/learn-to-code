print "Input [x] for exit."

while True:
	inp = raw_input("Tell me a number: ")
	if inp == "x":
		break
	try:
		number = float(inp)
	except ValueError:
		print "I said : Tell me a NUNBER!"
	else:
		test = number % 2
		if test == 0:
			print int(number), "is even."
		elif test == 1:
			print int(number), "is odd."
		else:
			print number, "is very strange"
		