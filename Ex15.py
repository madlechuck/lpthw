# imports argument vector from sys module
from sys import argv
# argument 1 is the script name, argument 2 should be the name of the file
# assigns filename to a value named filename
script, filename = argv
# The open command with the filename variable as a parameter is assigned to
# a variable named lire_fichier
lire_fichier = open(filename)
# tells you the name of the file
print "Here's your file %r" % filename
#prints the content of the file with the read function on the lire_fichier var.
print lire_fichier.read()
#same as before, but with a prompt from raw_input
print "Type the filename again:"
file_again = raw_input ("> ")
# assigns the open command to a new variable with argument variable from raw_input
txt_again = open(file_again)
# prints the content of the file with the read function on the txt_again variable
print txt_again.read()
close(filename)
close(file_again)
