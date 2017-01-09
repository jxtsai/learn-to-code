# check leap year


year = int(raw_input("enter a year: "))
if year % 4 == 0 and year % 100 != 0:
	print "The Year  IS a leap year"
elif year % 400 == 0:
	print "The Year  IS a leap year"
else:
	print "The Year  is NOT a leap year"
 


