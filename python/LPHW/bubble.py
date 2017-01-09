# algothrim bubble sort
import random

box = []
for i in range(0,8):
	box.append(random.randrange(1, 1000, 1))

print box 

min = box[0]
for i in box:
    if min > i:
        min = i
    else:
        min = min 

print min
print box.index(min)


