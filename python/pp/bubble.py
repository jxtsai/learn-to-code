# algothrim bubble sort
import random

box = []
for i in range(0,8):
	box.append(random.randrange(1, 1000, 1))

print box 

for i in range(0, len(box)):
	for j in range(0, len(box)-1):
		if box[j] > box[j+1]:
			tmp = box[j+1]
			box[j+1] = box[j]
			box[j] = tmp
    	
print box
