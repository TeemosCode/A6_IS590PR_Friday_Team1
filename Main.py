# from Map_Info import Info as info # a dictionary data structure

## Just paste and use it as module input would be easier
import Navigate as Nav


class UI():
    navi = Nav.Map()  # navigator that contains our Graph object, 'G'.
    # The choice for connecting userinput to corresponding data for calculation of smallest path. Grab the mail codes for the path function via this dictionary
    choice_mail_building = {str(choicenum): (buildingInfo[0], buildingInfo[1], buildingInfo[2]) for
                            choicenum, buildingInfo
                            in zip(range(1, len(navi.Buildings) + 1), navi.Buildings)}

    def menu(self, main_menu):
        """
        Shows menu

        :param main_menu: The keyword for deciding which menu to display
        """
        if main_menu:
            print("""
 =========================== Welcome to NaviGrapher ============================
 -------- Please Enter the "number" of choices below to use NaviGrapher --------
 (1). List all buildings
 (2). Navigate! 
 (3). Run all navigation tests
 (4). Exit 
			 """)

        if not main_menu:

            print("""
    ======================================= Navigation Mode ========================================
     Choose the corresponding NUMBER of TWO buildings where you would like to navigate between.
     You will be asked to choose the number of the building two times.
     First time will be the starting building of where you want to start.
     Second will be the building of the destination you want to arrive at.
    =========================== Choice : (Buildings, Address, Mailcode) ============================
            """)
            # Scalability for menu function. If there were more nodes added into the MapInfo.py, it can be uploaded accordingly without hardcoding in the first place.
            for numChoice in range(1, len(self.choice_mail_building) + 1):
                print("%2d: %s" % (numChoice, self.choice_mail_building[str(numChoice)]))

            print('%2d: \033[1mEnd Navigation Mode\033[0m\n' % (len(self.choice_mail_building) + 1))

    def Input_check_for_dummies(self, main_menu: int, decision=0) -> str:
        """
        The fucntion that takes in user inputs and validates the input, outputs the validated input

        :param main_menu: 0 or 1 to indicate which menu the program is currently desplaying
        :param decision: default to 0, used to grab the strings in the list variable 'keyword' for different promt message
        :return user_input: The string type of the valid user input
        """
        # check to see which menu is currently on display to change the valid choices coreespondingly
        if main_menu:
            choices = [str(n) for n in range(1, 5)]
            question_str = "Enter your Choice: "  # guide for users in different modes
        else:
            choices = [str(n) for n in range(1, len(self.navi.Buildings) + 2)]
            keyword = ["Choose your 'STARTING' building No.: ", "Choose your 'DESTINATION' building No.: "]
            question_str = keyword[decision]

        user_input = input(question_str)

        # The loop where dumb users will have to keep trying until they input the valid choices
        while user_input not in choices:
            print(
                "Invalid choice! NaviGrapher can not correctly execute!\nPlease ReEnter one of these choices: '{}' !".format(
                    choices))
            user_input = input(question_str)
        return user_input

    def naviGrapher_funcs(self, user_choice: str, main_menu: int) -> int:
        """
        The main action mapping fucntion. Takes valid user input and matches the corresponding function to for particular action.

        :param user_choice: The string of the valid user choice input
        :return main_menu: The numbers 0 or 1 to indicate the displaying menu
        """
        # If user chooses for Navigation, change the menu and switch to navigation mode.
        if main_menu and user_choice == "2":
            main_menu = 0
            # navigation_mode, if user chooses for navigation mode, Navigavtion program
            while True:
                self.menu(main_menu)
                user_Start = self.Input_check_for_dummies(main_menu)
                if user_Start == str(len(
                        self.choice_mail_building) + 1):  # Generalize the ending choice, make it scalable wihtout hardcoding
                    print("Aborting Navigation ....\n")
                    main_menu = 1
                    break
                start = self.choice_mail_building[user_Start][
                    2]  # get the mail code in our dictionary "choice_mail_building" tuple value with index 2

                user_Destination = self.Input_check_for_dummies(main_menu,
                                                                1)  # Changes the prompt string with the second parameter
                if user_Destination == str(len(self.choice_mail_building) + 1):
                    print("Aborting Navigation ....\n")
                    main_menu = 1
                    break
                end = self.choice_mail_building[user_Destination][
                    2]  # get the mail code in our dictionary "choice_mail_building" tuple value with index 2

                print("\n")
                print('=====================Starting Navigation=======================')
                self.navi.cal_path(start, end)

                print("======================End Of Navigation========================")
                print("\n")

        # Functions and actions matching the main menu choices
        elif main_menu and user_choice=='3':
            self.test_all_cases()
        elif main_menu:
            self.navi.print_buildings()

        return main_menu

    def test_all_cases(self):
        """
        Function that runs through all options of valid inputs starting and ending positions of buildings for testing if all nodes and paths
        are correctly implemented.

        If it there are no errors, it would keep run through all compositions of starting and ending building positions and print "Passed TESTS".
        Else it prints out the error and shows which two choices of buildings caused the error.
        """
        main_menu = 0
        while True:
            # prints our corresponding menu
            self.menu(main_menu)
            # get and validate user inputs

            # Testing all cases of travels between all buildings, if theres is no error, prints "Passed TESTS"
            try:
                for strtchoice in range(0, len(self.navi.Buildings) ):
                    #start_choice = str(strtchoice)
                    start_choice = self.navi.Buildings[strtchoice][2]
                    for endchoice in range(0, len(self.navi.Buildings)):
                        #end_choice = str(endchoice)
                        end_choice = self.navi.Buildings[endchoice][2]

                        # The navigation function to calculate the shortest paths in the graph function in Navigate.py
                        self.navi.cal_path(start_choice, end_choice)
            except:
                print("There occurs an error")
            else:
                # If there are no errors that disrupt the program, we pass the test
                print("Passed tests without error")
                break

    def run(self):
        main_menu = 1

        while True:
            # prints our corresponding menu
            self.menu(main_menu)
            # get and validate user inputs
            user_input = self.Input_check_for_dummies(main_menu)

            # When user chooses to end the program
            if user_input == "4" and main_menu:
                print("Thank you for using NaviGrapher. GoodBye~!")
                break
            # keep track of what menu to display
            main_menu = self.naviGrapher_funcs(user_input, main_menu)


if __name__ == "__main__":
    ui = UI()
    #ui.test_all_cases()
    ui.run()
