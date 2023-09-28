'''
已解


Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

solution:
filter() ?

'''



def unique_in_order(sequence):
    unique = [] 
    for i in range(len(sequence)-1):
        if sequence[i] != sequence[i+1]:
            unique.append(sequence[i])       
    if unique[-1] != sequence[-1]:
        unique.append(sequence[-1])
        return unique
    else:
        return unique
                

test = unique_in_order("AAAABBBCCDAABBB")
print(test)