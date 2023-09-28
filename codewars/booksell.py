'''
https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.

stocklist "L" ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
 a list of categories "M" ["A", "B", "C", "W"]

In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

task
to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category. 


'''

def stock_list(list_of_art, list_of_cat):
    
    l_l = [ l.split(" ") for l in list_of_art] 
    # 拆開 list_of_art
    for a in list_of_cat:
        for l in range(len(l_l)):
            if a == (l_l[l][0][0]):
                l_l[l].append(l_l[l][1])
                 
              
    print(l_l)                
                    


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
test = stock_list(b, c)

print(test)