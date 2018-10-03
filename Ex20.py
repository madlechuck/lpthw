# imports the sys module to get the arg variables/values
from sys import argv
# unpacks the inputted argument as input_file variable
script, input_file = argv
# functions  to read the whole file
def print_all(f):
    print f.read()
#functions to go back at the beginning of the file (rewind)
def rewind(f):
    f.seek(0)
# functions that prints a line from a file from the first value
def print_a_line(line_count, f):
    print line_count, f.readline()
# sets the files a a variable
current_file = open(input_file)

print "First let's print the whole file:\n"
# prints all with this fucntion
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# returns at the begginning
rewind(current_file)

print "Let's print four lines:"
# give the current_line variable a value then print incrementally by increasing
# the variable at each line by 1.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
