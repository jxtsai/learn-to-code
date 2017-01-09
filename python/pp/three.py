while True:
	print "Enter two number"
	num1 = raw_input("Enter the first number: ")
	num2 = raw_input("Enter the second number: ")
	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
	    print "You have enter NUMBER!"	
	else:
		if num1 + num2 > 100:
			print "That is  big number, the program would be terminate!"
			break
		else:
			print "The answer is ", num1 + num2


