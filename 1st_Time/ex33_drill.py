i = 0
numbers = []

def loopage(i):
	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)

		i = x + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		#return x
loopage(i)
print "The numbers: "

for num in numbers:
	print num