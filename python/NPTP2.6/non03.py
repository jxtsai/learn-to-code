def abslute_value(n):
    if n < 0:
        n = -n
    return n

a = 23
b = -23

if abslute_value(a) == abslute_value(b):
    print "The abslute value of %d and %d are equal" % (a, b)
else:
    print "The abslute value of %d and %d are not equal" % (a, b)

         
