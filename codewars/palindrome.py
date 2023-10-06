'''
longest_palindrome
https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python


Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0. 

'''

def palindrome(s):
    '''
    
    '''
    l = len(s)
    half = l // 2
    c = 0
    if l % 2 == 0: # even
        for i in range(half):
            if s[i] == s[0-l+i]:
                c = c + 2
            else:
                c = c
    else:
        for i in range(half):
            if s[i] == s[0-l+i]:
                c = c + 2
            else:
                c = c
    return c

def longest_palindrome (s):

    # Your code goes in here
    #
    pass
    
test = palindrome("abba") 
print(test)