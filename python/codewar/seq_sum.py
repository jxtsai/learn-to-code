'''
find the max sum of a sequence number 
return the sum
解法：
使用 i,j 兩個變數來控制陣列的長短，雙迴圈跑全部可能性，以找出其中的最大值


'''
import random

test_list = random.choices(range(-50, 100), k= 15)
print(test_list)

def seq_sum(array):
    max_val = sum(array)
    l = len(array)
    for i in range(l):
        for j in range(l):
            #print(f"i is {i}, j is {j}", end = "\t")
            if sum(array[j:i+1]) > max_val:
                max_val = sum(array[j:i+1])
    return max_val      

test = seq_sum(test_list)
print(test)