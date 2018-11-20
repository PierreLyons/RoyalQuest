# Setting description
# Prompt name
# Set quest
def start():
	print("What is your name?")
	name = input("> ")
	# return name
	entrance(name)



# entrance
	# right - mud_closet
	# straight - prep_room
def entrance(name):
	print(f"{name}, you have entered a dark and dingy hallway. ")
	print("To your right is a small mudroom.")
	print("Ahead is a door at the end of the entrance.")
	print("What do you wish to do?")
	print("1) Check out the mudroom.")
	print("or")
	print("2) Go through the door at the end of the entrance.")
	
	choice = int(input("Your choice (1 or 2): "))
	
	print(f"You've chosen: {choice}.")
	if choice == 1 or choice == "one":
		mud_closet()
	elif choice == 2 or choice == "two":
		prep_room()
	else:
		print(f"{name} you idiot! It's simple. 1 or 2. That's it.")
		print("Try again.")
		choice = int(input("Your choice (1 or 2): "))

def mud_closet():
	print("mudcloset")
	
def prep_room():
	print("prep")
# mud_closet
	# riddle - hint about going down and right
# prep_room
	# riddle
	# straight - stairs
# stairs
	# up - front_hallway
	# down - garden
# front hallway
	# door1 - bedroom1
	# door2 - bedroom2
# bedroom1
	# hint about reading
	# bookshelf - garden
	# door - bedroom2
# bedroom2
	# door - servant_hallway
# servant hallway
	# right_door - spiral_stairs
	# left_door - kitchen
# spiral stairs
	# riddle
	# door - observatory
# observatory
	# fight bonus
	# door - kitchen
# kitchen
	# door -  garden
# garden
	# right_door - shed
	# left_door - crypt
# shed
	# hint for bossfight
# crypt

start()	