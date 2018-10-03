line = "-" * 66

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

def input_temp():
	print "Please enter temperature to convert:\n"
	print line
	print "\n"
	return int(raw_input(">"))

		
def get_unit():
	print "\n"
	print "Convert to Farenheit(f) or Celcius(c)?"
	return raw_input(">")
	
print "\n\n"
print line
print "Welcome to the temperature converter!\n"

temp = input_temp()

unit = get_unit()
	
if unit == "f":
	tempf(temp)
elif unit == "F":
	tempf(temp)
elif unit == "C":
	tempc(temp)
elif unit == "c":
	tempc(temp)
else:
	print "Please choose between f or c."


	

