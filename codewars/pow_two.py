'''
檢查數字 x 是否為 2 之乘方
已解

'''

def power_of_two(x):
    if x == 0:
        return False
    elif x == 1 or x == 2:
        return True
    else:
        while x > 1:
            if x % 2 == 0:
                x = x // 2
            else:
                return False
            print(x)       
        return True     
 

test = power_of_two(4096)

print(test)