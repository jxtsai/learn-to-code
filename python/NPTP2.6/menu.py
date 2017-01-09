menu_item = 0
namelist = []
while  menu_item !=9:
	print "-" * 15
	print "1. Print the list"
	print "2. Add a name to the list"
	print "3. Remove a name from the list"
	print "4. Change an item in the list"
	print "9. Quit"
	menu_item = input("Pick an item from the menu: ")
	if menu_item == 1:
		current = 0
		if len(namelist) > 0:
			while current < len(namelist):
				print current, ".", namelist[current]
				current += 1
		else:
		    print "List is empty"
	elif menu_item == 2:
	    name = raw_input("Type in a name to add: ")
	    namelist.append(name)
	elif menu_item == 3:
	    del_name = raw_input("What name would you like to remove? ")
	    if del_name in namelist:
	    	item_number = namelist.index(del_name)
	    	del namelist[item_number]
	    else:
	    	print del_name, "was not found"
	elif menu_item == 4:
	 	old_name = raw_input("What name would you like to change? ")
	 	if old_name in namelist:
	 		item_number = namelist.index(old_name)
	 		new_name = raw_input("What is the new name? ")
	 		namelist[item_number] = new_name
	 	else:
	 		print old_name, "was not found"

print "Goodbye"



