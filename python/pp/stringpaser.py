list1 = [1, 4, 4, 5, 3, 2, 3, 2, 1, 6, 7]
visted = []
i = 0
while i < len(list1):
	if list1[i] in visted:
		list1.pop(i)
		continue
	visted.append(list1.pop(i))
	i += 1

print list1
print visted