def my_first_function(arg1,arg2):
	return (arg1 * arg2) / 2
	print "\n"

#1
print my_first_function(8, 4)

#2
print my_first_function(4 + 4, 2 + 2)
	
#3
x = 8
y = 4
print my_first_function(x, y)

#4
print my_first_function(x + 16 / 2 - 8, y - x + 8) 

#5
print "Please, tell me what file I should use:"
user_input = raw_input("\n>")

in_file = open(user_input)

argx = int(in_file.readline(1))
argy = int(in_file.readline(2))
print my_first_function(argx, argy)

#6
print "Please press 8"
arg1a = int(raw_input("Press '8' then enter:"))
print "Please press 4"
arg1b = int(raw_input("Press '4' then enter:"))
print my_first_function(arg1a, arg1b)