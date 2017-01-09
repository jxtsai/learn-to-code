import random

number = random.randrange(100)
guess = 0

while guess != number:
    guess = input("Guess a number from 0 to 99: ")
    if guess > number:
        print "Too high"
    elif guess < number:
        print "Too low"
print "Just rights!"