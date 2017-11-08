import MapInfo as mp
import Main_ as M
# ======MapInfo with a class======
# map = mp.MapInfo()
# print(map.Buildings)

# ======MapInfo without a class ======
# print(mp.Buildings)

navi = M.Map() # navigator that contains our Graph object, 'G'.

MI = mp.MapInfo() # MI: for Map Info. The Edges and Verix of the map to be added to the navi graph
print(MI.Buildings[14][2])
# print(navi)

##########  intialize our map graph ######
navi.add_buildings(MI.Buildings) # add all building nodes
navi.add_intersections(MI.Intersections) # add all intersections
navi.add_entries(MI.Entries) # add all entries
navi.add_diEdges(MI.DiEdges) # Add all directed edges
navi.add_undiEdges(MI.UndiEdges) # Add all undirected edges
navi.add_entryPaths(MI.EntryPaths) # Add all entry paths

# print(navi.G.edges)
# print(navi.G.adj)


# The choice for connecting userinput to corresponding data for calculation of smallest path. Grab the mail codes for the path function via this dictionary
choice_mail_building = { str(choicenum) : (buildingInfo[0], buildingInfo[2]) for choicenum, buildingInfo in zip( range(1, len(MI.Buildings) + 1 ) , MI.Buildings)}
##choice_mail_building[str(len(MI.Buildings) + 1)] = end_navigation_mode() # A provisional name for the fucntion --> MAY work on that later

# print(choice_mail_building)
print(choice_mail_building)

def menu(main_menu):
	"""
	Shows menu
	"""
	if main_menu:
		print("""
 =========================== Welcome to NaviGrapher ============================
 -------- Please Enter the "number" of choices below to use NaviGrapher --------
 (1). List All Buildings
 (2). List All Avaiable Paths
 (3). List All Entries to Certain Buildings
 (4). Navigate! 
 (5). Exit/Quit 
			 """)

	if not main_menu:
		print(
		"""
 Choose the corresponding NUMBER of TWO buildings where you would like to navigate between.
 You will be asked to choose the number of the building two times.
 First time will be the starting building of where you want to start.
 Second will be the building of the destination you want to arrive at.
=========================== Choice : (Buildings, Address, Mailcode) ============================
1 : ('School of Information Sciences', '501 E. Daniel St.', 493),
2 : ('Illini Union BookStore', '807 S. Wright St.', 312),
3 : ('Altgeld Hall', '1409 W. Green St.', 382),
4 : ('Illini Union', '1401 W. Green St.', 384),
5 : ('Henry Administration Building', '506 S. Wright St.', 339),
6 : ('English Building', '608 S. Wright St.', 718),
7 : ('Lincoln Hall', '702 S. Wright St.', 456),
8 : ('Gregory Hall', '810 S. Wright St.', 462),
9 : ('Main Library', '1408 W. Gregory Dr.', 522),
10: ('Institute For Genomic Biology', '1206 W. Gregory Dr.', 195),
11: ('Smith Memorial Hall (Music)', '805 S. Matthews Ave.', 56),
12: ('Foreign Languages Building', '707 S. Matthews Ave.', 166),
13: ('Davenport Hall', '607 S. Matthews Ave.', 148),
14: ('UI Ice Arena', '406 E. Armory Ave.', 525),
15: ('Armory', '505 E. Armory Ave.', 528)
16: ["End Navigation Mode"]
		""")

def Input_check_for_dummies(main_menu: int) -> str:
	"""
	The fucntion that takes in user inputs and validates the input, outputs the validated input

	:param main_menu: 0 or 1 to indicate which menu the program is currently desplaying
	:return user_input: The string type of the valid user input
	"""
	# check to see which menu is currently on display to change the valid choices coreespondingly
	if main_menu:
		choices = [str(n) for n in range(1,6)]
		question_str = "Enter your Choice: ==>  " # guide for users in different modes
	else:
		################## how to interchange the keyword questions??????
		choices = [str(n) for n in range(1, len(MI.Buildings) + 2)]
		keyword = ["Enter your STARTING position: ==> ", "Enter your DESTINATION: ==> "]
		question_str = "Enter your STARTING position: ==> "

	user_input = input(question_str)

	# The loop where dumb users will hav to keep trying until they input the valid choices
	while user_input not in choices:
		print("Invalid choice! NaviGrapher can not correctly execute!\nPlease ReEnter one of these choices: '{}' !".format(choices))
		user_input = input(question_str)
	return user_input


##### For Testing Purpose #####
# A dict with choice string and its corresponding function name
def myprint():
	print("Hi its working")
func_dict_main = {
	"1": navi.print_buildings,
	"2": navi.print_paths, # provisional functions to be later coded into the main.py to list out all paths
	"3": navi.print_entries, # provisional functions to be later coded into the main.py to list out entries
	"4": myprint
}

func_dict_navi = {
	"1": myprint,
	"2": myprint,
	"3": myprint,
	"4": myprint,
	"5": myprint,
	"6": myprint
}
##### For testing purpose ####
def naviGrapher_funcs(user_choice: str, main_menu: int) -> int:
	"""
	The main action mapping fucntion. Takes valid user input and matches the corresponding function to for particular action.

	:param user_choice: The string of the valid user choice input
	:return main_menu: The numbers 0 or 1 to indicate the displaying menu
	"""
	# If user chooses for Navigation, change the menu and switch to navigation mode.
	if main_menu and user_choice == "4":
		main_menu = 0
		# navigation_mode()  ---> To be continued for user choosing two numbers indicating starting and ending buildings maill code (ill do it later on)
	
	# Functions and actions matching the main menu choices
	elif main_menu:
		func_dict_main[user_choice]()

	# Navigation Functions and actions matching its menu  ################### Main play goes here now!!!!
	# May needa split into two functions for less generalized actions (it'll be easier i think,from where i am currently, brain stuck ... lol)
	else:
		func_dict_navi[user_choice]()
	return main_menu

def main():
	"""
	Main Fucntion to run the whole program
	"""
	main_menu = 1
	while True:
		# if user chooses for navigation mode, Navigavtion program
		while not main_menu:
			menu(main_menu)
			user_Start = Input_check_for_dummies(main_menu)

			if user_Start == "16":
				print("Aborting Navigation ....\n")
				main_menu = 1
				break
			start = choice_mail_building[user_Start][1] # get the mail code in our dictionary


			user_Destination = Input_check_for_dummies(main_menu)

			if user_Destination == "16":
				print("Aborting Navigation ....\n")
				main_menu = 1
				break
			end = choice_mail_building[user_Destination][1]


			print('=====================Starting Navigation=======================')
			print("\n")

			navi.cal_path(start, end)
			print("\n")




		else: ##
			menu(main_menu)
			# get and validate user inputs
			user_input = Input_check_for_dummies(main_menu)
			
			#When user chooses to end the program
			if user_input == "5" and main_menu:
				print("Thank you for using NaviGrapher. GoodBye~!")
				break
			# keep track of what menu to display
			main_menu = naviGrapher_funcs(user_input, main_menu)

main()





