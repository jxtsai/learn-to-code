'''
https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python


未解


to check wheter a given integer is a perfect power. If it is a perfect power, return a pair m and k with mk = n as a proof. Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.

Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.

ex:
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None


'''

import math

def isPP(num):
    '''
    2^2 = 4 可開根號
    2^3 = 8 無法開根號
    2^5 = 32 無法開根號
    number == math.pow(base, n) n 為奇數(質數)
    如何找出 base ? ==> base 介於 1 < base < log2n
    
    '''
    n = math.log2(number)
    base = math.sqrt(number) # 基數不應超過其開根號 + 1
    if base % 1 == 0:
        return int(base), int(base)
        
        
        
    while base > 1:
        if base % 2 != 0: # 奇數時
            number == math.power(base, n)  # 如何控制 n 的漸增與其邊界?
            base = base // 2
            
  
        