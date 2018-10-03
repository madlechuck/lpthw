name = 'Mathieu Langlois'
age = 38 # not a lie
height = 68 # inches
weight = 239.6 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_KG = weight / 2.2

print "Let's talkk about %s." % name
print "He's %d inches tall." % height
print "Hes's %d pounds heavy." % weight
print "In kilogram, that's %s kg" % weight_KG
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d."  % (
    age, height, weight, age + height + weight)
print weight_KG
