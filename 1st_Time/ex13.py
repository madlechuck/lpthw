from sys import argv

script, first, second, third = argv


print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

x = raw_input("Is this clear?")
y = raw_input ('say again?')

print "So you just said: %r and %r using the %r thing that came to your mind..." % (x, y, first)