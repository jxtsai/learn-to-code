sum = 0

print "Welcome to the average calculator program"

count = int(raw_input("How many numbers would you like to sum:"))
current_count = 0

while current_count < count:
	print "Number", current_count
	number = float(raw_input("Enter a number: "))
	sum = sum + number
	current_count += 1
print "The average was:", sum / count

