def mult(a, b): # this function will keep repeating itself
    if b == 0:
        return 0
    rest = mult(a, b - 1) # step3 once it reach This, the sequence starts over again and go  back to the top!
    value = a + rest
    return value # therefore, "return value" will not happen until the program gets past step 3 above

print "3 * 2 = ", mult(3, 2) # the "mult" function will first initate here


# the return value event at the end can therefor only happen once b equal to zero 
# (b decreased by 1 everytines step 3 happens)
