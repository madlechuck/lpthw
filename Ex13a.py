from sys import argv

script, x, y, a, b = argv
value = raw_input("Please enter a number:" )
print "x = %s" % (x)
print "y = %s" % (y)
print "a = %s" % (a)
print "b = %s" % (b)
print "x + y = %s" % (int(x) + int(y))
print "%s + %s = %s" % (x, y, int(x) + int(y))
print "You entered %s as a value!" % (value)
