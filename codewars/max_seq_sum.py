'''
找到一串陣列中某區間(或為全部)連續數之和的最大值
已解, 但不夠優化

https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

find the max sum of a sequence number 
return the sum
解法：
使用 i,j 兩個變數來控制陣列的長短，雙迴圈跑全部可能性，以找出其中的最大值


max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)

他人最佳解法
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max


'''

def max_sequence(array):
    neg = [a for a in array if a < 0]
    if len(array) == len(neg):
        return 0
    elif len(array) == 0:
        return 0
    positive = [a for a in array if a > 0]
    if len(array) == len(neg):
        return sum(array)
        
    max_val = sum(array)
    l = len(array)
    for i in range(l):
        for j in range(l):
            #print(f"i is {i}, j is {j}", end = "\t")
            if sum(array[j:i+1]) > max_val:
                max_val = sum(array[j:i+1])
    return max_val      
    
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))    
# print(max_sequence([-11, -6, -10, -32, -26, -34]))