from sys import argv  #imports sys module to use argv
script, input_file = argv  # script is the script name, input file is the file we want to use.

def print_all(f):  # Defines a function to print all the file.
	print f.read()  # This line will print the file content.
	
def rewind(f): # Defines a function to return at the beginning of the file.
	f.seek(0) # seek the first line of the file defines in the argument f.

def print_a_line(line_count, f):  # Defines a function that will print a line of a file.
	print line_count, f.readline()  # prints two arguments, one that will number the line and the other will print the dictated line.
	
current_file = open(input_file)  #Defines the variable current_file to open the file used in argv. 

print "First let's print the whole file:\n" #Print this text and then a return line.

print_all(current_file)  # Activates the function print all using the variable current_file that calls the file used in the command line as an argument.

print "Now let's rewind, kind of like a tape."  # Print this text.

rewind(current_file) #  Activates the function rewind using the argument file given in the argv.

print "Let's print three lines:" # Prints this text.

current_line = 1 # Gives a value of 1 to the variable current_line.
print_a_line(current_line, current_file)  # Calls the function print_a_line with a defines variable of 1 and using the file used in argv.

current_line = current_line + 1  #  Changes the variable current_line from 1 to 2, using a +1.
print_a_line(current_line, current_file) # Calls the function print_a_line with a new defined variable of 2 and using the file used in argv.

current_line = current_line + 1 # Changes the variable current_line from 2 to 3, using a +1 once again.
print_a_line(current_line, current_file)  # Calls the function print_a_line with a defined variable of 3 and using the filed used in argv.