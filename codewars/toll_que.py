'''
未解


https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!
input

    customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
    n: a positive integer, the number of checkout tills.

output

The function should return an integer, the total time required.
Important

Please look at the examples and clarifications below, to ensure you understand the task correctly :)


array of customer : 不會改動排隊次序

將 array 拆成 n 個小隊
   array_1  = [0, n+1, ..]
   array_2  = [1, n+2, ...]
   array_n = [n, n+n, ...]
       
best solution by others

def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
    
    
'''

def queue_time(customers, n):
    
    for  i in range(n):
        '''
        把 array 變成 n 個小隊
        '''
        for c in array:
            a.append(c)
            
