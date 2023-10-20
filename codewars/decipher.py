
'''
已解
Decipher this

https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python

You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

    the second and the last letter is switched (e.g. Hello becomes Holle)
    the first letter is replaced by its character code (e.g. H becomes 72)

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'

'''

def decipher_this(s):
    s_l  = s.split(" ")
    s_l_w = []
    
    for each in s_l:
        digits = ""
        letters = ""
        for l in each:
            if l.isdigit():
                digits = digits + l
            elif l.isalpha():
                letters = letters + l
        s_l_w.append([digits, letters])    
    res = []
    for e in s_l_w:
        if len(e[1]) > 1:
            res.append(chr(int(e[0]))+e[1][-1]+e[1][1:-1]+e[1][0])
        else:
            res.append(chr(int(e[0]))+e[1])
    return " ".join(res)        
    
test = decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp")
print(test)