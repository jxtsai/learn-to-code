
def eureka(n):
    '''
    check n is eureka number or not 
    ex 135 = 1**1 + 3 **2 + 5**3
    1 = 1**1
    8 = 8 ** 1
    89 = 8 **1 + 9** 2
    '''
    
    n_str = str(n)
    sum = 0
    for i, d in enumerate(n_str):
        sum = sum + int(d)**(i+1)
    
    if sum == n:
        return True
     
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    return (list(filter(eureka, list(range(a, b+1)))))
 

test = sum_dig_pow(1, 200)
print(test) 
    