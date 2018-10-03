from sys import argv

cravb, filename = argv
cravbe, filename = argv
readfile = open(filename)

print "Here is the content of %r." % filename

print readfile.read()

readfile.close()
