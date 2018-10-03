# imports the exit function from sys
from sys import exit

inv = []

def gold_room():
	# lets define the gold room
	print "This room is full of gold.  How much do you take? (Please, leave some for other players...)"  # Description of the room
	
	how_much = raw_input("> ")  
	# Players enters amount of gold taken
	# We then check if the input is an integer, else we restart the function
	try: 
		greed_test(int(how_much)) 
		#We try to run the function with the variable as an integer
	except ValueError:  
	# If the variable is not an integer, we print an error message and loop the function
		print("Please write an amount in number!")
		gold_room()
		
	
def greed_test(y):
	if y < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = prompt_s(bear_room)
		
		if choice == "take honey":
			dead("The bear looks at you then charges.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.  You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		elif choice == "kill bear":
			print "With wath???"
			bear_room()
		elif choice == "move bear":
			print "Ohhh, a tough guy huh??"
			bear_room()
		elif choice == "look":
			print "There is a bear here and he doesn't seem happy about your presence... You also notice a spear on the floor..."
			bear_room()
		else:
			print "I got no idea what that means."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for life or eat your head?"
	
	choice = prompt_s(cthulhu_room)
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "you are dead!  Try again!"
	exit(0)

def prompt_s(go_back):
	x = raw_input(":>")
	
	if x == "inventory":
		print inv 
		go_back()
	elif x == "inv":
		print inv
		go_back()
	else:
		return x
		
	
def start():
	sr_left_door = False
	if "key" in inv:
		sr_left_door = True
	print "\nYou are in a dark room."
	
	if "key" not in inv:
		print "You see a key on the floor."
	
	print "There is a door to your right and left."
	print "What do you do?"
	
	choice = prompt_s(start)
	
	if choice == "left" and sr_left_door == False:
		print "The door is locked!"
		start()
	elif choice == "left" and sr_left_door  == True:	
		print "You unlocked the door with the key and proceed to the next room..."
		bear_room()
	elif choice == "right":
		cthulhu_room()
	if choice  == "take key":
		if "key" not in inv:
			inv.append("key")
			print "You put the key in your inventory"
			start()
		else:
			print "You already have the key!"
			start()
	else:
		print "I don't understand that command!"
		start()

		
start()
