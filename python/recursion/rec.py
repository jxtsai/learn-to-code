'''
factorial 
'''


def recur(n):
    if n == 1:
        return 1
    else:
        return n *  recur(n-1)


test = recur(5)

print(test)