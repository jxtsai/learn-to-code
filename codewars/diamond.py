'''
https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python




''''



def diamond(n):
    # Make some diamonds!
    """
    " " 增到減又減到增. "*" 1 增到 n (odd) 又再減到 1
    
    """
    if n < 0 or n % 2 == 0:
        return None
    half = n //2
    s = ""
    w = ""
    for i in range(1, n+1, 2):
        s = s + " " * half+"*"*i +"\n"
        half = half - 1      
    h = 1    
    for i in range(n-2, 0, -2):
        w = w + " " * h+"*"*i + "\n"
        h = h + 1 
    return s + w  


test = diamond(2)
print(test)