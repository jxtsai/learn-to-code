'''
已解

https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.

stocklist "L" ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
 a list of categories "M" ["A", "B", "C", "W"]

In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

task
to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category. 

smart ans:
def stock_list(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ""
    result = ""
    for cat in listOfCat:
        total = 0
        for book in listOfArt:
            if (book[0] == cat[0]):
                total += int(book.split(" ")[1])
        if (len(result) != 0):
            result += " - "
        result += "(" + str(cat) + " : " + str(total) + ")"
    return result
    
    

'''

def stock_list(list_of_art, list_of_cat):
    l_l = [ l.split(" ") for l in list_of_art] 
    # 拆開 list_of_art
    
    stock = dict()
    for c in list_of_cat:
        stock[c] = []
    for c in list_of_cat:
        for i in range(len(l_l)):  
            if c == l_l[i][0][0]:
                stock[c].append(l_l[i][1])
            else:
                stock[c].append("0") 
    
    for k, v in stock.items():
        stock[k] = sum(int(x) for x in v )
    
    if sum( v for v in stock.values()) == 0:
        return ""
    else: 
        return " - ".join((f"({k} : {v})") for k, v in stock.items()) 