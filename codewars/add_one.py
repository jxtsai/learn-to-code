'''
https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

examples:

[4, 3, 2, 5] would return [4, 3, 2, 6]
[1, 2, 3, 9] would return [1, 2, 4, 0]
[9, 9, 9, 9] would return [1, 0, 0, 0, 0]
[0, 1, 3, 7] would return [0, 1, 3, 8]

'''

def up_array(arr):
    pass #your code here
    if len(arr) == 0:
        return None
    for n in arr:
        if n < 0 or n >= 10:
            return None
    # 先排除 arr 當中會出現負數或多位數等狀況   
     
    arr_str = "" # 將 arr 連成字串資料型態
    for a in arr:
        arr_str = arr_str + str(a)
    res = int(arr_str) + 1
    if len(str(res)) < len(arr):
        final = [0]
        for n in str(res):
            final.append(int(n))
    else:
        final = [int(n) for n in str(res)]
    
    return final 
    
    
test  = up_array([0,1,9,9])
print(test)