
data = [9, 3, 2, 8, 7, 5, 6, 1, 4]

for i in range(0, len(data)):
	tmp = data[i]
	j = i
	while data[j-1]>tmp & j >=1:
		data[j] = data[j - 1]
		j -= 1

	data[j] = tmp
	print data[j]

print data



