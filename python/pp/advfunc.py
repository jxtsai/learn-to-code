def mult(a, b):
    if b == 0:
        return 0
    rest = mult(a, b -1)
    value = a + rest
    return value

result = mult(3, 2)
print " 3 * 2 = ", result


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print "2! = ", factorial(2)
print "3! = ", factorial(3)
print "4! = ", factorial(4)
print "5! = ", factorial(5)
