from sys import argv
#unpack arguments
script, filename = argv
#tells that it will erase the content of the file given as argument to filename variable
print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."
#enter answer
raw_input("?")

print "Opening the file..."
# opens the file given as argv with the 'w' parameter
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
# erases the content of the file
target.truncate()

print "Now I'm going to ask you for three lines."
#creates three variables from raw_input
line1 = raw_input ("line 1: ")
line2 = raw_input ("line 2: ")
line3 = raw_input ("line 3: ")

print "I'm going to write these to the file."
# writes the variables on three lines using the write function and enter.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
#closes the file
target.close()
