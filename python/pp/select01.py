# algothrim selection sort
import random

box = []
for i in range(0,8):
	box.append(random.randrange(1, 1000, 1))
print box 

for i in range(0, len(box)):
	min = box[i]
	count = 0
	for j in range(0, len(box)):
		if box[j] < min:
			min = box[j]
			pos = j
	print min, pos
	tmp = box[i] 
	box[i]= min
	box[pos] = tmp

print box
