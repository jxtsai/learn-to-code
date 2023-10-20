'''
Ordered Count of Characters

https://www.codewars.com/kata/57a6633153ba33189e000074/train/python

'''

def ordered_count(inp):
    inp_set = set(inp) # unique char
    uniq_order= []
    for i in inp:
        if i in inp_set:
            uniq_order.append(i)
    return [(i, inp.count(i)) for i in uniq_order]
        
 
test= ordered_count('abracadabra')
print(test)