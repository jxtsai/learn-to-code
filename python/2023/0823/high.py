import string
from functools import reduce


def scores(str):
    total = 0
    for x in str:
        total = total + string.ascii_lowercase.index(x)
    return total    


def high(arr):
    l_arr = arr.split(" ")
    s_list = list(map(scores, l_arr))
    highest = max(s_list)
    return l_arr[s_list.index(highest)]
    

test = high("abde dffd schol savd")
print(test)    
