# algothrim bubble sort
box = [4, 2, 5, 1, 9, 7, 3, 6, 8]

for i in range(0, len(box)):
	for j in range(0, len(box)-1):
		if box[j] > box[j+1]:
			tmp = box[j+1]
			box[j+1] = box[j]
			box[j] = tmp
    	

print box
