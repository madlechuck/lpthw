name = 'Mathieu Langlois'
age = 34 # not a lie
height = 68 # inches
weight = 205 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

# This will convert the height in cms
height_cm = height * 2.54

#This will convert the weight in KGs
weight_kg = weight / 2.2


print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d centimetres!" % height_cm
print "He's %d pounds heavy." % weight
print "That's %d kilograms!" % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
