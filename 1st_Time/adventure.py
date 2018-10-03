print "You are alone, in a dark room."
print "1. You stay where you are."
print "2. You light a match."

choix = int(raw_input(">"))
if choix == 1:
	print "You stay where you are and think that this is boring..."
elif choix == 2:
	print "You light a match and can now see your surroundings!"
	print "There is a desk in front of you, a door to your right and a monster on the floor"
	print "1. Open the desk"
	print "2. Open the door"
	print "3. Kick the monster"
	choix2 = int(raw_input(">"))
	if choix2 == 1:
		print "you opened the desk and found what you were looking for, congratulations..."
	elif choix2 == 2:
		print "You opened the door and found the exit.  Congratulation..."
	elif choix2 == 3:
		print "You kicked the monster and killed it. You are victorious!  Congratulations..."
	else:
		print "You are too dumb to play!"
else:
	print "You are too dumb to play!"
