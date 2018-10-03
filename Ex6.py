# creating variable x, including a format that is 10
x = "There are %d types of people." % 10
# assigns variable binary
binary = "binary"
# assigns variable do_not
do_not = "don't"
# assigns variable y to a string with 2 formats that use previous variables
y = "Those who know %s and those who %s." % (binary, do_not)
#prints variable x then y
print x
print y
#prints more stuff using the same previous variables
print "I said: %r." % x
print "I also said: '%s'." % y
# sets variable hilarious
hilarious = False
# sets variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"
# prints the joke with the answer on the same line
print joke_evaluation % hilarious
# sets variables w and e
w = "This is the left side of..."
e = "a string with a right side."
# prints variable w then e on after the other
print w + e
