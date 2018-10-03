def tempf(temp):
	result = (9 / 5) * temp + 32
	print "\n\n"
	print line
	print "%d degrees Celcius equals %d degrees Farenheit." % (temp, result)
	print line
	print '\n'
	
def tempc(temp):
	result = (5 / 9) * (temp - 32)
	print "\n\n"
	print line
	print "%d degrees Farenheit equals %d degrees Celcius." % (temp, result)
	print line
	print '\n'

line = "-" * 66

print "\n\n"
print line
print "Welcome to the temperature converter!\n"

def input_temp():
	print "Please enter temperature to convert:\n"
	print line
	print "\n"
	try:
		return int(raw_input(">"))
	except ValueError:
		print "Please enter a number!"
		input_temp()
    
temp = input_temp()


	
print "\n"
print "Convert to Farenheit(f) or Celcius(c)?"

unit = raw_input(">")

if unit == "f" or "F":
	tempf(temp)
elif unit == "c" or "C":
	tempc(temp)
else:
	print "Please choose between f or c."
