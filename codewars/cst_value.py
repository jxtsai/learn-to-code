'''
已解


Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"


best solution by others

def solve(s):
    return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))
    
'''
import string



def solve(string):
    letters = "0abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    '''
    先把英文字串各別字母 依其 index 位置分數作成一個列表
    
    母音的分數為  0
    '''
    l = []
    for s in string:
        if s in vowels:
            l.append(0)
        else:
            l.append(letters.index(s))
            
    print(l)       
    '''
    對參雜 0 的列表, 以零作為區隔來計算連續和之最大值
    
    '''        
    con_add = 0
    max_add = l[0]
    for n in l:
        if n != 0 and max_add > con_add:
            con_add = con_add + n
            max_add = max_add
        elif n != 0 and max_add <= con_add:
            con_add = con_add + n
            max_add = con_add
        elif n == 0 and max_add <= con_add:
            max_add = con_add
            con_add = 0
        elif n == 0 and max_add > con_add:
            max_add = max_add
            con_add = 0
            
        print(n, max_add, con_add)    
    
    return max_add
  
test = solve("khrushchev")
print(test)