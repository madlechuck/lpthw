x = "fatso"
y = "tomo"

print "Hey,", x, "\b!  Are you coming today or", y, "\brrow?"

print """
Hey %s! Are you coming today or %srrow?
"""  % (x, y)

answer = raw_input("Tell me:")
print "What? You think you can just tell me \"%s\" and get away with it?"  % answer