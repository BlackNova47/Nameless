#Joseph Ahn
#CSC119
#Text Based Adventure
import random
import time
Gold = 0
Health = 100
Mana = 100
# ***ATTRIBUTES***
Stength = 0
Agility = 0
Intelligence = 0

def clearscreen():
	print("\n" * 100)
	user_choice =""
def enterName():
	clearscreen()
	print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
	print('''                                                         ENTER YOUR NAME                      ''')
	print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')
	print('''                                                                                              ''')

def attributeStart():
	clearscreen()
	print('''                                              ==============================                 ''')
	print('''                                               ASSIGN YOUR ATTRIBUTE POINTS                  ''')
	print('''                                               ============================                  ''')
	print('''                              [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] ''')
	print('''                                                                                             ''')
	print('''                                                                                             ''')





	print('''                                                                                             ''')
	print('''                                                                                             ''')
	print('''                              [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	print('''                                                                                                ''')
	user_enter = str(input("                                                  Press Enter To Continue "))
	if user_enter == '':
		clearscreen()
		enterName()

def start_event():
	event_options = ["1","2","3"]
	user_choice =""
	while user_choice not in event_options:
		clearscreen()
		print('''      _______________________________________________________________________________________ ''')
		print('''    /|     -_-                                             _-      _-                       | ''')
		print('''   / |_-_- _                                         -_- _-   -   _-  _--                   | ''')
		print('''     |                            _-  _--                                                   | ''')
		print('''     |                            ,                            _-,  _--                     | ''')
		print('''     |      .-'````````'.        '(`        .-'```````'-.       '(`      .-'```````'-.      | ''')
		print('''     |    .` |           `.      `)'      .` |           `.     `)'    .` |           `.    | ''')
		print('''     |   /   |             \      U      /   |             \     U    /   |             \   | ''')
		print('''     |  |    |              | o   T   o |    |              |    T   |    |              |  | ''')
		print('''     |  |    |              |  .  |  .  |    |              |    |   |    |              |  | ''')
		print('''     |  |    |              |   . | .   |    |              |    |   |    |              |  | ''')
		print('''     |  |    |              |    .|.    |    |              |    |   |    |              |  | ''')
		print('''     |  |    |______________|     |     |    |______________|    |   |    |______________|  | ''')
		print('''     |  |   /  __ ;   -     |     !     |   /     `    _ -  |    !   |   /     --        |  | ''')
		print('''     |  |  / __            -|        -  |  /  __--      -   |        |  /                |  | ''')
		print('''     |  | /        __-- _   |   _- _ -  | /        __--_    |   - _  | /        __--_    |  | ''')
		print('''     |__|/__________________|___________|/__________________|________|/__________________|__| ''')
		print('''    /                                             _ -                   -_                  | ''')
		print('''   /   -_- _ -             _- _---                       -_-  -_                   -_       | ''')


		print('''
				=============================================================
				The dungreon greets you with three doors which will you take?
				=============================================================
					
					1) The first door.
					2) The second door.
					3) The third door. 
			
			''')
		user_choice = str(input("Enter Option Number: "))
		#print("You have selected " + user_choice)
	if user_choice == event_options[0]:
		room01()
	elif user_choice == event_options[1]:
		room02()
	elif user_choice == event_options[2]:
		room03()
def room01():
	clearscreen()
	print("\n \n --> You have entered room1")
def room02():
	clearscreen()
	print("\n \n --> You have entered room2")
def room03():
	clearscreen()
	print("\n \n --> You have entered room3")

def thisUserIsAnIdiot():
	clearscreen()
	user_enter = str(input(" Just press the Enter key, dont type anything dumbass."))
	if user_enter == '':
		attributeStart()
	else:
		clearscreen()
		print('''I'm sorry, can you not read? Cause if thats the case I dont think you should be playing a TEXT BASED ADVENTURE buddy.       Press ENTER to continue, do not type ANYTHING OTHER THAN ((((ENTER))))) ''')




def displayTitlescreen():
	print("                                   ______ _   _ _   _ _____  _____ _____ _   _       ")
	print("                                   |  _  \ | | | \ | |  __ \|  ___|  _  | \ | |      ")
	print("                                   | | | | | | |  \| | |  \/| |__ | | | |  \| |      ")
	print("                                   | | | | | | | . ` | | __ |  __|| | | | . ` |      ")
	print("                                   | |/ /| |_| | |\  | |_\ \| |___\ \_/ / |\  |      ")
	print("                                   |___/  \___/\_| \_/\____/\____/ \___/\_| \_/      ")
	print("                                                                                     ")
	print("                                                                                     ")
	print("                                          ___________   _____ _   _  _____           ")
	print("                                         |  _  |  ___| |_   _| | | ||  ___|          ")
	print("                                         | | | | |_      | | | |_| || |__            ")
	print("                                         | | | |  _|     | | |  _  ||  __|           ")
	print("                                         \ \_/ / |       | | | | | || |___           ")
	print("                                          \___/\_|       \_/ \_| |_/\____/           ")
	print("                                                                                     ")
	print("                                                                                     ")
	print("                                _   _   ___  ___  ___ _____ _      _____ _____ _____ ")
	print("                               | \ | | / _ \ |  \/  ||  ___| |    |  ___/  ___/  ___|")
	print("                               |  \| |/ /_\ \| .  . || |__ | |    | |__ \ `--.\ `--. ")
	print("                               | . ` ||  _  || |\/| ||  __|| |    |  __| `--. |`--. |")
	print("                               | |\  || | | || |  | || |___| |____| |___/\__/ /\__/ /")
	print("                               \_| \_/\_| |_/\_|  |_/\____/\_____/\____/\____/\____/ ")
	print("                                                                                     ")
	user_enter = str(input("                                              Press Enter To Continue "))
	if user_enter == '':
		attributeStart()
	else:
		thisUserIsAnIdiot()


displayTitlescreen()
