'''
已解

The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If
    sz is <= 0 or if str is empty return ""
    sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".


example
revrot("123456987654", 6) --> "234561876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "44668753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> "" 
revrot("563000655734469485", 4) --> 

'''

def rev_rot(strng, sz):
    
    if sz is <= 0 or if strng == "" :
        return ""
    elif sz >len(strng):
        return ""
        
    # Step 1 分割原字串   
    c = 0
    strng_list = []
    while (sz)*c < len(strng):
        if len(strng[sz*c:sz+(sz*c)]) == sz:
            strng_list.append(strng[sz*c:sz+(sz*c)])
        c = c + 1
    # Step 2 對各字串元素進行檢查
    res = []     
    for i in range(len(strng_list)):
        sum_x = sum(int(x) for x in strng_list[i])
        if sum_x % 2 == 0:
            strng_list[i] = strng_list[i][::-1] # 該字串反向
        else:
            strng_list[i] = strng_list[i][1:]+strng_list[i][0] # 該字串向左移一位, 第一個字成為最後字
    return "".join(strng_list)            
    
test = rev_rot("563000655734469485", 4)

print(test)