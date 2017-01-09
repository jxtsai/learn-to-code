# check prime a
import math

a = int(raw_input("enter a number: "))
b = 2
if(a % b != 0):
	print "a IS a Prime number"
	b = b + 1
	b <= math.sqrt(a)
else:    
    print "a is NOT a Prime number" 
 


