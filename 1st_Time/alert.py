from sys import exit
from time import sleep

# First let's create a little text animation.
def intro(x):
	sleep(x)
	print "\n.",
	sleep(x)
	print ".",
	sleep(x)
	print ".",
	sleep(x)
	print "Alert!\n",

def help():
	print """\nHere is a list of commands:
	- Help:  List of commands
	- Look:  Look around you
	- Hint:  Gives you a hint
	- Use "ITEM":  Use an item from your inventory
	- Quit:  Quit the game"""

def input():

	name = raw_input("\nPlease, enter your name:>")

def start():
	for _ in range(3):
		intro(.75)
	print "\n\"Commander %s, it is time to evacuate.  Wake up commander %s...\"" % (name, name)
	for _ in range(2):
		intro(.75)
	print "\nA distant voice speaks to you.  You slowly regain consciousness..."
	for _ in range(1):
		intro(.75)
	print "\n\"Commander %s, you must evacuate immediately!  Please respond commander %s..." % (name, name)
	sleep(3)
	print """\nAs you open your eyes, everything is coming back to you in a flash."
The admiral's last order was to hold your ground, even before seeing the Samor's
pulsating rays cutting through rows and rows of class 5 destroyers from your Armada,
you knew this would be his last...  Your remember the chaos aboard the Radicor,
your jetspire frigate, as all the other ships started coming apart around you.  You recall
ordering your crew to use the pods to escape, but to no avail, they would never let you
fight alone.  Thousand of debris were flying toward your ship.  The Radicor suffered critical
damage from a detached mass-reactor from one of the destroyers.	The shock was so brutal that
the hull got breached in several places. The ship's O2 reserves are all empty, you only have
the remaining safety oxygen from the bridge private recycler.  Your whole crew probably suffocated
or got jettisoned on impact.  The sound from the alarm is screaming in your ears as the ship's ai
is literally yelling at you:"""
	raw_input("Please, press \"ENTER\" to continue...")
	print "\n\"It is good to see you awake sir."
	sleep(2)
	print "\n\"The oxygen level are too low, you must put on your combination sir."
	sleep(2)
	print "\n\"Please proceed according to protocol \"F\" and put on your combination in order to escape the ship."


# intro "animation"

start()
