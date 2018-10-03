from sys import argv

script, str = argv

def reverse(list):
	print list
	reverse_list = []
	y = len(list) - 1
	#print "Y value at beginning is %r" % y
	#print "reverse list at beginning contains: %r" % reverse_list
	#print " lenght of list is of: %r " % len(list)
	while y >= 0:
		reverse_list.append(list.pop(-1))
		print reverse_list
		y = len(list) - 1
	else:
		str = ''.join(reverse_list)
		return str
		

		


def FirstReverse(str): 
	list = []
	for x in str:
		list.append(x)
	#print list
	str = reverse(list)
	return str
	
	


	
print FirstReverse(str)


	
#print revdlst  