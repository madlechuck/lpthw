# defines a function called cheese_and_crackers that prints text using two arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# prints the function using the numbers 20 and 30 as arguments.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# prints the function using variables instead of just numbers.
print "OR, we can use variables from our script:"
#  Here we define the variables.
amout_of_cheese = 10
amout_of_crackers = 50
# Here, we place the variables as arguments.
cheese_and_crackers(amout_of_cheese, amout_of_crackers)
# Here we use two additions for arguments.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#  Here, we use both the variables defined earlier and add 100 and 1000 to them as arguments.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amout_of_cheese + 100, amout_of_crackers + 1000)