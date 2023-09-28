'''
找出質數與其差

The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

    g (integer >= 2) which indicates the gap we are looking for

    m (integer > 2) which gives the start of the search (m inclusive)

    n (integer >= m) which gives the end of the search (n inclusive)

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.

找出介於 m ~ n 之間的質數，兩個連續質數差等於 g
請傳回第一組質數,若無則傳回 None


'''

def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True        
            

def prime_list(m, n):
    '''
    傳回 m~n  之間的質數
    '''
    return[ i for i in range(m, n+1) if prime_number(i)]

def gap(g, m, n):
    # your code
    prime_numbers = prime_list(m, n)
    print(prime_numbers)
    for i in range( len(prime_numbers)-1):
        if  prime_numbers[i+1] - prime_numbers[i] == g:
            return [prime_numbers[i], prime_numbers[i+1]]
        
    return None
    


test =gap(4,100,110)

print(test)