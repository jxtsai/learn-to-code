'''
https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

找出陣列中某二個數值其加為 n-1

已解, 但算法不夠優化

Sum of Pairs

Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.
sum_pairs([11, 3, 7, 5], 10) >>> [3, 7]

method array 為 n個數字 則可能有 (n-1)n/2 之可能性
array 無法 sorted 排列?

def sum_any(array) >>> 傳回 array 所有可能的二個數字加總之組合 (list or tuple)
    pos = []
    c = 1
    for i in range(len(array)-1):
        arr[i] + arr[i+c]
        c = c + 1

'''
# def sum_pairs(array, add):
    # for a in sum_any(array):
        # if a == add:
            # return True
        # else:
            # return False

# def sum_pairs(array, add):
    # for i in range(len(array)-1):
        # for x in range(i+1, len(array)):
            # if add == array[i]+array[x]:
                # return array[i], array[x]
        
    # return None     

def sum_pairs(ints, s):
    d = set() # 預作為 difference 差之集合
    for n in ints:  # loop list
        if n in d:  # 檢查 n 是否在 set 當中
            return [s - n, n] 
        d.add(s - n) # 在不重覆的集合中加入 二數之差
    
        
test = sum_pairs([5, 9, 13, -3], 10)
print(test)