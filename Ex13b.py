from sys import argv

script, name = argv
print "\n"
print "Hello %r, what is you last name? " % (str(name)),
last_name = raw_input()
print ".-.-.-.\n" * 10,
print ".-.-.-.\n" * 10,
print ".-.-.-.\n" * 10,
print "Hello %s %s" % (name, last_name)
print ".-.-.-." * 10
print ".-.-.-." * 10
print ".-.-.-." * 10
