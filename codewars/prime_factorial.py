'''
已解
https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :
 "(p1**n1)(p2**n2)...(pk**nk)"
 

解題思路

先求n 所有的因數 dec factors(n) ==> return list of all factors
處理factors list

best solution from other folks

def primeFactors(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n%i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0: pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1
        
    return r
        
'''


from functools import reduce

def factors(n):
    try: 
        return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
    except TypeError:
        return []
                
def prime_number(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True  

def prime_factors(n):
    prime_list = [x for x in  factors(n) if prime_number(x)]
    if prime_list == []:
        return "("+str(n)+")"
    prime_list.sort()
    prod = []
    test = []
    for p in prime_list:
        f = 0
        while n % p**f ==0:
            f = f+ 1
        prod.append(f-1)    
    for i in range(len(prod)):
        if prod[i] == 1:
            test.append("("+str(prime_list[i])+")")
        else:    
            test.append("("+str(prime_list[i])+"**"+str(prod[i])+")")
         
    return "".join(test)
    
test = prime_factors(7919)
print(test)
    
    