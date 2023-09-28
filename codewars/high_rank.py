'''
https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python

已解

傳回陣列參數中，出現頻率最多次的數字, 若該數字為一個以上，則取其中最大值者


Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.


思路:

別人聰明的方法
from collections import Counter

def highest_rank(arr):
    if arr:
        c = Counter(arr)
        m = max(c.values())
        return max(k for k,v in c.items() if v==m)
'''

def highest_rank(arr):
    uniq = set(arr) # 先拆去列表重覆的數字
    most = max(list(arr.count(n) for n in uniq)) # 找出最高的出現次數
    arr_by_v = sorted(arr, reverse = True) #以數值由大至小重新排列, 以便立即找到符合的最大值
    
    for n in arr_by_v:
        if arr_by_v.count(n) == most:
            return n
    
    
test = highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12])
print(test)