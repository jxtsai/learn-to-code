def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crakcers!" % boxes_of_crackers
	print "Man that's enought for a party"
	print "Get a blankedt. \n"
# make a function name cheese_and_crackers which take both amount as their argument



print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30) #call the function cheese_and_crakcers with arguments20,30. so it would print out the three line with the amount


print "Or, we can use variables from our script: "
amout_of_cheese = 10
amount_of_crackers = 50
# make twp variables as the function's arguments so it's easier to updated or change


cheese_and_crackers(amout_of_cheese, amount_of_crackers)

print "We can even do math inside too."
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math: "
cheese_and_crackers(amout_of_cheese+100, amount_of_crackers+1000)

