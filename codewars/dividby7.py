'''
https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/python

A number m of the form 10x + y is divisible by 7 if and only if x − 2y is divisible by 7. In other words, subtract twice the last digit from the number formed by the remaining digits. Continue to do this until a number known to be divisible by 7 is obtained; you can stop when this number has at most 2 digits because you are supposed to know if a number of at most 2 digits is divisible by 7 or not.


m = 371 -> 37 − (2×1) -> 37 − 2 = 35 ; thus, since 35 is divisible by 7, 371 is divisible by 7. 

m = 477557101->47755708->4775554->477547->47740->4774->469->28 and 28 is divisible by 7, so is 477557101. The number of steps is 7.


recursion function ?

The original number is divisible by 7 if and only if the last number obtained using this procedure is divisible by 7. 


'''
def rec_7(n):
    return n//10 - (n % 10) * 2


def seven(m):
    # your code
    c = 0
    while m > 100:
        m = rec_7(m)
        c = c + 1
    if m % 7 == 0:
        return m, c

test = seven(483595)
print(test)