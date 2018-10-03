x = "There are %d types of people." % 10 # defines how many type of people there are (in binary)
binary = "binary"  #defines variable binary
do_not = "don't"  #defines variable do_not
y = "Those who know %s and those who %s." % (binary, do_not)   #defines variable y

# theses two lines prints the joke made of x and y
print x
print y
# These two repeats the joke as a quote in between single quotes.
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False  # Defines variable hilarious
joke_evaluation = "Isn't that joke so funny?! %r"  # defines variable joke_evaluation

print joke_evaluation % hilarious  #prints joke evaluation and uses a string in it to place the hilarious variable

w = "This is the left side of...  "  # defines variable w
e = "a string with a right side."    # defines variable e

print w + e   # prints a sentence using variables w and e