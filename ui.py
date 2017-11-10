#from Map_Info import Info as mpi # a dictionary data structure

## Just paste and use it as module input would be easier
import MapInfo as mpi
import Main as Map


navi = Map.Map() # navigator that contains our Graph object, 'G'.

# different approach
# ##########  intialize our map graph ######
# navi.add_buildings(mpi["Buildings"]) # add all building nodes
# navi.add_intersections(mpi["Intersections"]) # add all intersections
# navi.add_entries(mpi["Entries"]) # add all entries
# navi.add_diEdges(mpi["DiEdges"]) # Add all directed edges
# navi.add_undiEdges(mpi["UndiEdges"]) # Add all undirected edges
# navi.add_MQPaths(mpi["MainQuadPaths"]) # Add all paths to main quad
# navi.add_entryPaths(mpi["EntryPaths"]) # Add all entry paths


##########  intialize our map graph ######
navi.add_buildings(mpi.Buildings) # add all building nodes
navi.add_intersections(mpi.Intersections) # add all intersections
navi.add_entries(mpi.Entries) # add all entries
navi.add_diEdges(mpi.DiEdges) # Add all directed edges
navi.add_undiEdges(mpi.UndiEdges) # Add all undirected edges
navi.add_MQPaths(mpi.MainQuadPaths) # Add all paths to main quad
navi.add_entryPaths(mpi.EntryPaths) # Add all entry paths



# The choice for connecting userinput to corresponding data for calculation of smallest path. Grab the mail codes for the path function via this dictionary
choice_mail_building = { str(choicenum) : (buildingInfo[0], buildingInfo[1], buildingInfo[2]) for choicenum, buildingInfo in zip( range(1, len(mpi.Buildings) + 1 ) , mpi.Buildings)}


#print(choice_mail_building)

def menu(main_menu):
	"""
	Shows menu

	:param main_menu: The keyword for deciding which menu to display
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
      =========================== Navigation Mode ============================
 Choose the corresponding NUMBER of TWO buildings where you would like to navigate between.
 You will be asked to choose the number of the building two times.
 First time will be the starting building of where you want to start.
 Second will be the building of the destination you want to arrive at.
=========================== Choice : (Buildings, Address, Mailcode) ============================
		""")
		# Scalability for menu function. If there were more nodes added into the MapInfo.py, it can be uploaded accordingly without hardcoding in the first place.
		for numChoice in range(1, len(choice_mail_building) + 1):
			print("%2d: %s" % (numChoice, choice_mail_building[str(numChoice)]))

		print('%2d: ["End Navigation Mode"]\n' % (len(choice_mail_building) + 1))

def Input_check_for_dummies(main_menu: int, decision = 0) -> str:
	"""
	The fucntion that takes in user inputs and validates the input, outputs the validated input

	:param main_menu: 0 or 1 to indicate which menu the program is currently desplaying
	:param decision: default to 0, used to grab the strings in the list variable 'keyword' for different promt message
	:return user_input: The string type of the valid user input
	"""
	# check to see which menu is currently on display to change the valid choices coreespondingly
	if main_menu:
		choices = [str(n) for n in range(1,6)]
		question_str = "Enter your Choice: ==>  " # guide for users in different modes
	else:
		choices = [str(n) for n in range(1, len(mpi.Buildings) + 2)]
		keyword = ["Choose your 'STARTING' position: ==> ", "Choose your 'DESTINATION': ==> "]
		question_str = keyword[decision]

	user_input = input(question_str)

	# The loop where dumb users will have to keep trying until they input the valid choices
	while user_input not in choices:
		print("Invalid choice! NaviGrapher can not correctly execute!\nPlease ReEnter one of these choices: '{}' !".format(choices))
		user_input = input(question_str)
	return user_input


##### For Testing Purpose #####
# A dict with choice string and its corresponding function name
def myprint():
	print("Hi its working")
##### For testing purpose ####


### This "Has" to be hard coded!
# Dictionary that maps user choices to corresponding functions in the graph object
func_dict_main = {
	"1": navi.print_buildings,
	# Currently use myprint test function to keep the program from crashing before the functions are finished and tested!!####
	"2": myprint, # navi.print_paths, # provisional functions to be later coded into the main.py to list out all paths
	"3": myprint, # navi.print_entries, # provisional functions to be later coded into the main.py to list out entries
	"4": myprint
}



def naviGrapher_funcs(user_choice: str, main_menu: int) -> int:
	"""
	The main action mapping fucntion. Takes valid user input and matches the corresponding function to for particular action.

	:param user_choice: The string of the valid user choice input
	:return main_menu: The numbers 0 or 1 to indicate the displaying menu
	"""
	# If user chooses for Navigation, change the menu and switch to navigation mode.
	if main_menu and user_choice == "4":
		main_menu = 0
		# navigation_mode, if user chooses for navigation mode, Navigavtion program
		while True:
			menu(main_menu)
			user_Start = Input_check_for_dummies(main_menu)
			if user_Start == str(len(choice_mail_building) + 1): # Generalize the ending choice, make it scalable wihtout hardcoding
				print("Aborting Navigation ....\n")
				main_menu = 1
				break
			start = choice_mail_building[user_Start][2] # get the mail code in our dictionary "choice_mail_building" tuple value with index 2


			user_Destination = Input_check_for_dummies(main_menu, 1) # Changes the prompt string with the second parameter
			if user_Destination == str(len(choice_mail_building) + 1):
				print("Aborting Navigation ....\n")
				main_menu = 1
				break
			end = choice_mail_building[user_Destination][2] # get the mail code in our dictionary "choice_mail_building" tuple value with index 2

			print("\n")
			print('=====================Starting Navigation=======================')
			navi.cal_path(start, end)

			print("======================End Of Navigation========================")
			print("\n")

	# Functions and actions matching the main menu choices
	elif main_menu:
		func_dict_main[user_choice]()

	return main_menu

def main():
	"""
	Main Fucntion to run the whole program
	"""
	main_menu = 1
	while True:
		# prints our corresponding menu
		menu(main_menu)
		# get and validate user inputs
		user_input = Input_check_for_dummies(main_menu)
		
		#When user chooses to end the program
		if user_input == "5" and main_menu:
			print("Thank you for using NaviGrapher. GoodBye~!")
			break
		# keep track of what menu to display
		main_menu = naviGrapher_funcs(user_input, main_menu)


if __name__ == "__main__":
	main()





