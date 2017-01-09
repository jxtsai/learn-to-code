answer = 23
question = "What number am I thinking of? "
print "Let's play the guessing grame!"

while True:
	guess = int(raw_input(question))
	if guess < answer:
		print "little Higher"
	elif guess > answer:
	    print "little Lower"
	else:
	    print "BINGO!"
	    break

	   	
   