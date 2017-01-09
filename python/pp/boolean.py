list = ["Life", "The Universe", "Everything", "Jack", "Jill", "Life", "Jill"]

copy = list[:]
copy.sort()
print copy, "The sorted list"
prev = copy[0]
print "I am prev", prev
del copy[0]
print copy, "The del index0"

count = 0
while count < len(copy) and copy[count] != prev:
	prev = copy[count]
	count += 1
print "I am the while", prev

if count < len(copy):
	print "First Match: ", prev