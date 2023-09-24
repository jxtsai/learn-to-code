'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.

Find the sum of all the multiples of 3 or 5 (from 1 to 1000)

'''

def multi_sum(n):
    '''
    1 to n , the sum of all the multiples of 3 or 5
    '''
    s_3 = sum(range(3, n, 3)) # 3 multiples 之和
    s_5 = sum(range(5, n, 5))
    s_15 = sum(range(15, n, 15))
    print(s_3, s_5, s_15)
    return s_3 + s_5 - s_15

test = multi_sum(30)
print(test)