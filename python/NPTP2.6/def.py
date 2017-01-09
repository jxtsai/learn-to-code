def hello():
    print "Hello"

def area(w, h):
    return w * h

def print_welcome(name):
    print "Welcome", name

hello()
hello()

print_welcome("Fred")
w = 4
h = 5
print "width = %d, height = %d , so the area = %d" %(w, h, area(w, h))

a = 4

def print_func():
    a = 17
    print "in print_func a = %d" % a

print_func()
print "a = %d which is global variable assigned prior to the function print_func" % a

a_var = 10
b_var = 15
c_var = 25

def a_func(a_var):
    print "in a_func a_var = ", a_var
    b_var = 100 + a_var
    d_var = 2 * a_var
    print "in a_func b_var = ", b_var
    print "in a a_func d_var = ", d_var
    print "in a a_func c_var =", c_var
    return b_var + 10

c_var = a_func(b_var)

print "a_var = ", a_var
print "b_var = ", b_var
print "c_var = ", c_var
print "d_var = ", d_var

