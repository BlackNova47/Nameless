#Joseph Ahn
#CSC119
#Text Based Adventure
import random
import time
Gold = 0
Health = 100
Mana = 100
# ***ATTRIBUTES***
maxPoints = 5
Strength = 5
Accuracy = 5
Agility = 5
Intelligence = 5

def clearscreen():
	print("\n" * 100)
	user_choice =""

def introScreen():
	print('''            ___  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ''')
	print('''             __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __) ''')
	print('''             ______)(______)(______)(______)(______)(______)(______)(______)(______)(______)(______)(______)(___ ''')
	print('''                                                                                                                 ''')
	print('''             You awaken on the cold stone floor in a dungeon room dimly lit by a torch mounted upon the two paths''')									
	print('''             entrances in front of you. Your thoughts are disrupted by a sharp pain as you try and recollect     ''')
	print('''             where you are, or even who you are. The only coherent thought you have is that the dungeon ahead    ''')
	print('''             holds answers, treasure, and more...                                                                ''')
	print('''                                                                                                                 ''')
	print('''                                                                                                                 ''')
	print('''                                                                                                                 ''')
	print('''                                                                                                                 ''')
	print('''                                                                                                                 ''')
	print('''                                                                                                                 ''')
	print('''              __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)(__  __)''')
	print('''            (______)(______)(______)(______)(______)(______)(______)(______)(______)(______)(______)(______)(___ ''')
	print("                                                 Press Enter To Continue ")
	print("\n" * 9)
	user_enterStart = str(input(""))
	if user_enterStart == '':
		start_event()


def enterName():
	clearscreen()
	print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
	print('''                                                         ENTER YOUR NAME                      ''')
	print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
	print("\n" * 11)
	user_name = str(input(" "))
	if user_name == '':
		clearscreen()
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                        YOU FOOL, DIDN'T YOU READ THE TITLE OF THE GAME???    ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_intro = str(input(" "))
		if user_intro == '':
			introScreen()
	else: 
		clearscreen()
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                        YOU FOOL, DIDN'T YOU READ THE TITLE OF THE GAME???    ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_intro = str(input(" "))
		if user_intro == '':
			introScreen()

def attributeStart():
	global maxPoints
	global Strength
	global Accuracy
	global Agility
	global Intelligence
	clearscreen()
	if maxPoints == 0:
		print('''                                       =====================================                 ''')
		print('''                                       You've distributed your skill points!                 ''')
		print('''                                              Press Enter To Continue!                       ''')
		print('''                                       =====================================                 ''')
		print("\n" * 11)
		user_entercon = str(input(""))
		if user_entercon == '':
			enterName()
		else:
			enterName()

	print('''                                              ==============================                 ''')
	print('''                                               ASSIGN YOUR ATTRIBUTE POINTS                  ''')
	print('''                                               ============================                  ''')
	print('''                                           You have %s unspent attribute points              ''' % maxPoints)
	print('''                              [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] ''')
	print('''                                                                                             ''')
	print('''                              [1](Strength) How much damage your attacks do.    : %s  '''% Strength)
	print('''                                                                                             ''')
	print('''                              [2](Accuracy) Your ability to hit targets.        : %s  '''% Accuracy)
	print('''                                                                                             ''')
	print('''                              [3](Agility) Your ability to run and dodge.       : %s  '''% Agility)
	print('''                                                                                             ''')
	print('''                              [4](Intelligence) Your ability to decypher.       : %s  '''% Intelligence)
	print('''                                                                                             ''')
	print('''                                                                                             ''')
	print('''                                                                                             ''')
	print('''                              [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] ''')
	print('''                               Distribute your points to your desired attributes by entering ''')
	print('''                               in the [number] corresponding with your desired attribute and ''')
	print('''                               hitting ENTER.                                                ''')
	print("\n" * 4)
	user_enterstat = str(input("                                         Enter Single Number [1-4]:   "))
	if user_enterstat == '1':
		Strength = Strength + 1
		maxPoints = maxPoints - 1
		clearscreen()
		attributeStart()

	else: 
		if user_enterstat == '2':
			Accuracy = Accuracy + 1
			maxPoints = maxPoints - 1
			clearscreen()
			attributeStart()
		else:
			if user_enterstat == '3':
				Agility = Agility + 1
				maxPoints = maxPoints - 1
				clearscreen()
				attributeStart()
			else:
				if user_enterstat == '4':
					Intelligence = Intelligence + 1
					maxPoints = maxPoints - 1
					clearscreen()
					attributeStart()
				else:
					clearscreen()
					print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
					print('''                                                                                              ''')
					print('''                                            Only enter a single number [1, 2 , 3, 4]          ''')
					print('''                                                                                              ''')
					print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
					user_enter = str(input("                                                  Press Enter To Continue "))
					if user_enter == '':
						clearscreen()
						attributeStart()

def web_event():
	event_options = ["1","2","3"]
	user_choice =""
	while user_choice not in event_options:
		clearscreen()
		print('''                                                         \    \_______/    /       ''')
		print('''                                                          `.,-'\_____/`-.,         ''')
		print('''                                                           /`..'\ _ /`.,'\         ''')
		print('''                                                          /  /`.,' `.,'\  \        ''')
		print('''                                                         /__/__/     \__\__\__     ''')
		print('''                                                         \  \  \     /  /  /___    ''')
		print('''                                                         /\  \,'`._,'`./  /\       ''')
		print('''                                                          /\,'`./___\,'`./\_\      ''')
		print('''                                                         /,'`-./__|__\,-'`.        ''')
		print('''                                                         / _  / __|__ \     \      ''')
		print('''                                                             /____|____\           ''')

		print('''
				=============================================================
				As you're brushing away small cobwebs you're halted by a  
				enormous spider web, the web seems thick and strong, however
				there does seem to be a gap you could fit though, but its high
			    up the web. What do you do?
				=============================================================
					
					1) Attempt to cut through the spider web.
					2) Observe surroundings for a solution.
					3) Try to jump through the gap.
			
			''')
		user_choice = str(input("Enter Option Number: "))
	if user_choice == event_options[0]:
		webroom01()
	elif user_choice == event_options[1]:
		webroom02()
	elif user_choice == event_options[2]:
		webroom03()

def webroom01():
	global Strength
	clearscreen()
	if Strength >= 7:
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                                                                              ''')
		print("                                   Your sword cleaves through the web, tearing a hole though it's")
		print('''                                 grid, allowing you to  walk right through.                    ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_enter = str(input("                                                   Press Enter To Continue "))
		if user_enter == '':
			clearscreen()
		else:
			clearscreen()
	else:
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                                                                              ''')
		print("                                   Within your first swing, you quickly realise your attempts will")
		print('''                                 do nothing to the huge web.                                   ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_enter = str(input("                                                   Press Enter To Continue "))
		if user_enter == '':
			web_event()
		else:
			web_event()




def webroom03():
	global Agility
	clearscreen()
	if Agility >= 7:
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                                                                              ''')
		print("                                   You leap into the after a good running start and slip right    ")
		print('''                                 through the hole in the web!                                 ''')
		print('''                                                                                              ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_enter = str(input("                                                   Press Enter To Continue "))
		if user_enter == '':
			clearscreen()
		else:
			clearscreen()
	else:
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                                                                              ''')
		print("                                   As you make your leap up, you realise mid air that there is no ")
		print('''                                 way you're making that jump. You collide with the web but    ''')
		print('''                                 manage to free yourself from its grasp.                      ''')
		print('''                                                                                              ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_enter = str(input("                                                   Press Enter To Continue "))
		if user_enter == '':
			web_event()
		else:
			web_event()







def spider_event(x):
	if(x==1000):
		enemyHealth = 13
	else:
		enemyHealth = x
	event_options = ["1","2","3"]
	user_choice =""
	while user_choice not in event_options:
		clearscreen()
		print('''                                                                 (                 ''')
		print('''                                                                  )                ''')
		print('''                                                                 (                 ''')
		print('''                                                          /\  .-"""-.  /\          ''')
		print('''                                                         //\\/  ,,,  \//\\         ''')
		print('''                                                         |/\| ,;;;;;, |/\|         ''')
		print('''                                                         //\\\;-"""-;///\\         ''')
		print('''                                                        //  \/   .   \/  \\        ''')
		print('''                                                       (| ,-_| \ | / |_-, |)       ''')
		print('''                                                         //`__\.-.-./__`\\         ''')
		print('''                                                        // /.-(Oo oO)-.\ \\        ''')
		print('''                                                       (\ |)   '---'   (| /)       ''')
		print('''                                                         `(|           |) `        ''')
		print('''                                                          \)           (/          ''')
		print('''
				=============================================================
				As you make your way down the poorly torchlit path a giant 
				spider quickly descends from the dungeon ceiling, nearly
				jumping entirely on top of you. It looks hostile as it blocks
				your path. What do you do?
				=============================================================
					
					1) Attack the Giant Spider!
					2) Use Item.
					3) Try to run past.
			
			''')
		user_choice = str(input("Enter Option Number: "))
	if user_choice == event_options[0]:
		spiderroom01(enemyHealth)
	elif user_choice == event_options[1]:
		spiderroom02()
	elif user_choice == event_options[2]:
		spiderroom03(enemyHealth)
def spiderroom01(enemyHealth):
	clearscreen()
	global Strength
	global Health
	global Accuracy
	global Gold
	attackAttempt = random.randint(3, 10)
	if attackAttempt + Accuracy < 13:
		clearscreen()
		enemydmg = random.randint(1, 10)
		Health = Health- enemydmg
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                                                                              ''')
		print("                                  Your attack fails and the Giant Spider does %s damage to you!"% enemydmg)
		print("                                                     You have %s health left"% Health)
		print('''                                                                                              ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_enter = str(input("                                                   Press Enter To Continue "))
		if user_enter == '':
			clearscreen()
			spider_event(enemyHealth)
		else:
			clearscreen()
			spider_event(enemyHealth)

	else:

		clearscreen()
		enemyHealth -= Strength
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                                                                              ''')
		print("                                  Your attack is succesful and you deal %s damage to the spider!" % Strength)
		print("                                                   The Giant spider have %s health left"% enemyHealth)
		print('''                                                                                              ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_enter = str(input("                                                   Press Enter To Continue "))
		if user_enter == '':
			if enemyHealth <= 0:
				clearscreen()
				addGold = random.randint(45, 85)
				Gold = Gold+ addGold
				print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
				print('''                                                                                              ''')
				print("                                      Your attack is succesful and you defeat the Giant Spider! ")
				print("                                                          You found %s gold coins!              " % addGold)
				print('''                                                                                              ''')
				print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
				print("\n" * 11)
				user_enter = str(input("                                                   Press Enter To Continue "))
				if user_enter == '':
					web_event()				
			else:
				clearscreen()
				spider_event(enemyHealth)
		else:
			clearscreen()
			addGold = random.randint(45, 85)
			Gold = Gold+ addGold
			print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
			print('''                                                                                              ''')
			print("                                      Your attack is succesful and you defeat the Giant Spider! ")
			print("                                                          You found %s gold coins!              " % addGold)
			print('''                                                                                              ''')
			print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
			print("\n" * 11)
			user_enter = str(input("                                                   Press Enter To Continue "))
			if user_enter == '':
				web_event()	

def spiderroom02():
	clearscreen()
	print("\n \n --> You have entered room2")
def spiderroom03(enemyHealth):
	global Health
	global Agility
	clearscreen()
	runAttempt = random.randint(1, 8)
	if runAttempt + Agility < 13:
		clearscreen()
		enemydmg = random.randint(1, 10)
		Health = Health- enemydmg
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                                                                              ''')
		print("                               Your attempt to run past the Giant Spider fails and you take %s damage!"% enemydmg)
		print("                                                     You have %s health left"% Health)
		print('''                                                                                              ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_enter = str(input("                                                   Press Enter To Continue "))
		if user_enter == '':
			clearscreen()
			spider_event(enemyHealth)
		else:
			clearscreen()
			spider_event(enemyHealth)

	else:

		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print('''                                                                                              ''')
		print('''                                            You succsessfully run past the Giant Spider!.     ''')
		print('''                                                                                              ''')
		print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
		print("\n" * 11)
		user_enter = str(input("                                              Press Enter To Continue "))
		if user_enter == '':
			clearscreen()
			spider_event(enemyHealth)
		else:
			clearscreen()
			spider_event(enemyHealth)

def start_event():
	introevent_options = ["1","2","3"]
	user_introchoice =""
	while user_introchoice not in introevent_options:
		clearscreen()
		print('''                                  _________________________________________________________    ''')
		print('''                                /|     -_-                                             _-  |\  ''')
		print('''                                 |                  _-        ,                -_- _-      |   ''')
		print('''                                 |      .-'````````'.        '(`        .-'``````'-.       |   ''')
		print('''                                 |    .` |>          `.      `)'      .` |           `.    |   ''')
		print('''                                 |   /   |>           <\      U      /   |             \   |   ''')
		print('''                                 |  |    |>            <| o   T   o |    |  o        O  |  |   ''')
		print('''                                 |  |    |>            <|  .  |  .  |>0< |  o o    o o  |  |   ''')
		print('''                                 |  |    |>            <|   . | .   |    |     o   o    |  |   ''')
		print('''                                 |  |    |>            <|    .|.    |    |              |  |   ''')
		print('''                                 |  |    |____;_________|     |     |>o< |____;_________|  |   ''')
		print('''                                 |  |   /  __     -     |     !     |   /      >0< _ -  |  |   ''')
		print('''                                 |  |  / __            -|        -  |  /  __--      -   |  |   ''')
		print('''                                 |  | /        __-- _   |   _- _ -  | /        __--_    |  |   ''')
		print('''                                 |__|/__________________|___________|/__________________|__|   ''')
		print('''                                /                                             _ -          \   ''')
		print('''                               /   -_- _ -             _- _---                      -_-  -_ \  ''')
		print('''
				=============================================================
				The dungreon greets you two paths, the left path seems to have
				some sort of spikes portruding from the side, while the right 
				path seems to have cowbwebs and small spiders crawing in and  
				out of the pathway. What will you do?                                          
				=============================================================
					
					1) Go down the left path.
					2) Go down the right path.
					3) Turn back. 
			
			''')
		user_introchoice = str(input("Enter Option Number: "))
	if user_introchoice == introevent_options[0]:
		room01()
	elif user_introchoice == introevent_options[1]:
		room02()
	elif user_introchoice == introevent_options[2]:
		room03()
def room01():
	clearscreen()
	print("\n \n --> You have entered room1")
def room02():
	clearscreen()
	spider_event(1000)
def room03():
	clearscreen()
	print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
	print('''                                                                                              ''')
	print('''                                  The large stone door behind you is shut, and does not budge.''')
	print('''                                                                                              ''')
	print('''                                  <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>''')
	print("\n" * 11)
	user_enter = str(input("                                                   Press Enter To Continue "))
	if user_enter == '':
		clearscreen()
		start_event()
	else:
		clearscreen()
		start_event()

	def start_event2():
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





def displayTitlescreen():
	start = False
	print("                                                                                      .---. ")
	print("                                                                                     /  .  |")
	print("                                                                                    |\_/|  |")
	print("                                                                                    |   | /|")
	print("           .------------------  ---------------------------------------------------------' |")
	print("          /  .-.              \/      ______ _   _ _   _ _____  _____ _____ _   _          |")
	print("         |  /   \                    |  _  \ | | | \ | |  __ \|  ___|  _  | \ | |          |")
	print("         | |\_.  |                   | | | | | | |  \| | |  \/| |__ | | | |  \| |          |")
	print("         |\|  | /|                   | | | | | | | . ` | | __ |  __|| | | | . ` |          |")
	print("         | `---' |                   | |/ /| |_| | |\  | |_\ \| |___\ \_/ / |\  |          |")
	print("         |       |                   |___/  \___/\_| \_/\____/\____/ \___/\_| \_/          |")
	print("         |       |                                                                         |")
	print("         |       |                          ___________   _____ _   _  _____               |")
	print("         |       |                         |  _  |  ___| |_   _| | | ||  ___|              |")
	print("         |       |                         | | | | |_      | | | |_| || |__                |")
	print("         |       |                         | | | |  _|     | | |  _  ||  __|               |")
	print("         |       |                         \ \_/ / |       | | | | | || |___               |")
	print("         |       |                          \___/\_|       \_/ \_| |_/\____/               |")
	print("         |       |                                                                         |")
	print("         |       |                                                                         |")
	print("         |       |                _   _   ___  ___  ___ _____ _      _____ _____ _____     |")
	print("         |       |               | \ | | / _ \ |  \/  ||  ___| |    |  ___/  ___/  ___|    |")
	print("         |       |               |  \| |/ /_\ \| .  . || |__ | |    | |__ \ `--.\ `--.     |")
	print("         |       |               | . ` ||  _  || |\/| ||  __|| |    |  __| `--. |`--. |    |")
	print("         |       |               | |\  || | | || |  | || |___| |____| |___/\__/ /\__/ /    |")
	print("         |       |               \_| \_/\_| |_/\_|  |_/\____/\_____/\____/\____/\____/     |")
	print("         |       |                                                               /\         / ")
	print("         |       |---------------------------------------------------------------  ------'  ")
	print("          \     /                                                                           ")
	user_enter = str(input("           `---'                              (Press Enter To Continue) "))
	if user_enter == '':
		attributeStart()
	else:
		clearscreen()
		user_enter = str(input(" Hey idiot,Just press the Enter key, dont type anything."))
		if user_enter == '':
			attributeStart()
		else:
			clearscreen()
			user_enter = str(input("Listen buddy, it really isnt that complicated. Do not type ANYTHING, just hit the ENTER key on your keyboard."))
			if user_enter == '':
				attributeStart()
			else:
				while start == False:
					clearscreen()	
					user_enter = str(input('''I'm sorry, can you not read? Cause if thats the case I dont think you should be playing a TEXT BASED ADVENTURE buddy.       Press ENTER to continue, do not type ANYTHING OTHER THAN ((((ENTER))))) '''))
					if user_enter == '':
						start=True
						attributeStart()
						 		
			
				


displayTitlescreen()