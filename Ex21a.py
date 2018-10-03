from sys import argv

script, val1, val2 = argv

def add(a, b):
    print "Adding %d to %d" % (a, b)
    print "result = %d" % (a + b)
    return a + b
def multiply(a, b):
    print "Multiplying %d by %d" % (a, b)
    print "result = %d" % (a * b)
    return a * b
def divide(a, b):
    print "Dividing %d by %d" % (a, b)
    print "result = %d" % (a / b)
    return a / b
def subtract(a, b):
    print "Subtracting %d from %d" % (b, a)
    print "result = %d" % (a - b)
    return a - b

def myfunction(x,y):
    print "creating something from %r and %r" % (x, y)
    x = int(x)
    y = int (y)
    add(x, y)
    print multiply(x, y)
    print divide(x, y)
    print subtract(x, y)

myfunction(val1, val2)


print subtract(15.0,subtract(35,multiply(8,divide(666.0, 33.0))))
