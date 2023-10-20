'''
https://www.codewars.com/kata/5375f921003bf62192000746/train/python

The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

    A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
    The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").


abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!"

'''
import string


puncs = string.punctuation
    
def punc(w):
    '''
    特殊符號處理
    '''
    res = []
    
    for l in w:
        if l in puncs:
           c = w.index(l) 
        else:
           c = c + 1 
           

def check_punc(w):
    for l in w:
        if  l in puncs:
            return True
    return False        
def abbreviate(s):
    s_list = s.split(" ")
    res = []
    for w in s_list:
        if check_punc(w):
            res.append(punc(w))
        else:
            if len(w) < 4:
                res.append(w)
            else: 
                res.append(w[0] +str(len(w) -2) + w[-1])
            
    return " ".join(res)
 
test = punc("elephant-ride!") 
#test = abbreviate("elephant-rides")    
print(test)
