from sys import argv

script, filename = argv

print "Opening file %s" % filename

lire_fichier = open(filename)

print lire_fichier.read()
lire_fichier.close()
