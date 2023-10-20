'''
https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python

Rotate for a Max

'''

def max_rot(n):
    max_res = 0
    str_n = [d for d in str(n)]
    for a in range(len(str_n)-1):
        

test = max_rot(56789)
print(test)