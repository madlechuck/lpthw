from sys import argv  #This imports the sys module so we can use argv.

script, filename = argv  # The first argument is the name of the script,
#the second need to be the name of the file you want to open, it gets the 
#filename variable name.

txt = open(filename)  #Opens the file using what was typed in the argv.

print "Here's your file %r:" % filename  #prints the name of the file.
print txt.read()  #Prints the content of the file.

print "Type the filename again:"  #asks a question.
file_again = raw_input("> ")  #defines the file_again variable using what is typed in.

txt_again = open(file_again)  #defines a variable that when used opens the file inputed on line 13.

print txt_again.read() #prints the content of the file.