def print_menu():
	print '1. Print Dictionary'
	print '2. Add definition'
	print '3. Remove word'
	print '4. Lookup word'
	print '5. Quit'
	print

words = {}
menu_choice = 0
print_menu()

while menu_choice != 5:
	menu_choice = input("Type in a number(1-5): ")
	if menu_choice == 1:
		print "Definition:"
		for x in words.keys():
			print x, ": ", words[x]
	elif menu_choice == 2:
		print "Add definition"
		name = raw_input("Word: ")
		means = raw_input("Definition: ")
		words[name] = means
	elif menu_choice == 3:
	    print "Remove word"
	    name = raw_input("word: ")
	    if name in words:
	        del words[name]
	        print name, "was removed."
	elif menu_choice == 4:
		print "Look Word"
		name = raw_input("word: ")
		if name in words:
			print "The definition of ", name, "is ", words[name]
		else:
		    print "No definition for ", name, 'was found'	
	elif menu_choice != 5:
		print_menu()

