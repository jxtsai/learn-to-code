def apple_and_banana(apple,banana):
	print "The amount of apple is: %d in this blasket." % apple
	print "There are %d banana in this brasket as well." %banana


apple_and_banana(5, 6)

apple = int(raw_input("How many apple did you have yesterday? "))
banana = int(raw_input("Hwo many banana did you buy today? "))


print "Now we can update the amount of apple and banana now."
apple_and_banana(5-apple, 6+banana)


