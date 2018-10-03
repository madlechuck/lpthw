
from sys import argv
script, a, b, c = argv
print type(a)
print type(b)
print type(c)
def elephant(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    print type(a)
    print type(b)
    print type(c)
    print "Calculating the average for the arguments: "
    average = (a + b + c) / 3.0
    print "So %r + %r + %r divided by three is %r" % (a, b, c, average)
    print "\n"

elephant(a, b, c)

print "\n"
print ".......................    \n\n" *2
print "Heres what it is for 33, 439 and 52..."
elephant(33, 439, 52)



print "Heres what it is for 33, 439 and 52..."
elephant(469.62, 77.01, 535)


print "Please enter three numbers: \n"

h = float(raw_input("no 1:" ))
print "\n"
s = float(raw_input("no 2:" ))
print "\n"
o = float(raw_input("no 3:" ))
print "\n"
print "type of 1st = %r" % type(h)
print "type of 2nd = %r" % type(s)
print "type of 3rd = %r" % type(o)
print "\n"
elephant(h, s, o)
print "\n"

elephant(4+4, 5*5, 4/3.0)
