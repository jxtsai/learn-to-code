def collatz(n):
    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            print(collatz(n/2), end=" - - " )
            return 1+ collatz(n/2) 
        else:
            print(collatz((3*n) +1), end = "x") 
            return 1+ collatz((3*n) +1)  
        
    


test = collatz(3)
print(test)