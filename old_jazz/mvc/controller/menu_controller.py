class MenuController():

    def __init__(self):

        self.menu_choices = {"S": "Start",
                             "D": "Difficulty",
                             "A": "About",
                             "Q": "Quit"}

        self.difficulty_levels = {1: "Easy",
                                  2: "Medium",
                                  3: "Hard"}

        self.main_menu = None
        self.user_menu_choice = None

    def generate_menu(self):
        menu_choice_str = str(self.menu_choices).strip(
            "{}").replace(", ", "\n")
        default_menu = f"MAIN MENU\n{menu_choice_str}\n"
        if self.status == 1:
            menu = "\t\tWELCOME TO MASTERMIND\n\n" + default_menu
        elif self.status == 2:
            menu = default_menu
        elif self.status == 3:
            menu = "Thank you for playing MASTERMIND!\n" + default_menu
        return menu

    def get_game_intro(self, attempts):
        intro_0 = "Guess a four digit number made up of "
        intro_1 = "only numbers between 0 and 7 inclusive.\n"
        intro_2 = f"You have ONLY {attempts} attempts.\n"
        intro = intro_0 + intro_1 + intro_2
        return intro

    def get_about_msg(self):
        about = "\t\tABOUT\n"
        about_1 = "Your task is to guess a 4 digit number correctly "
        about_2 = "from a total of 8 different numbers.\nThe number "
        about_3 = "of attempts you have depends on your choosen "
        about_4 = "difficulty level.\nPossible Numbers: [0  1  2  3  4  5  6  7]"
        about_5 = "\nGOOD LUCK!\n"
        about_msg = about + about_1 + about_2 + about_3 + about_4 + about_5
        return about_msg

    def get_options_str(self, options: dict):
        options_str = str(options).strip("{}").replace(", ", "\n")
        return options_str

    def set_user_choice(self, msg: str, menu_type: dict, user_choice):

        pass

    def detect_menu_choice(self):
        while self.status != 4:
            self.user_menu_choice = self.get_menu_choice_str()
            self.menu_change = self.menu_change_detected()
            if self.menu_change:
                menu_set = self.set_main_menu()
                if menu_set:
                    self.previous_menu_choice = self.user_menu_choice
        return

    def menu_change_detected(self):
        if self.user_menu_choice != self.previous_menu_choice:
            self.menu_change = True
        else:
            self.menu_change = False
        return self.menu_change

    def set_main_menu(self):
        chosen = False
        while not chosen:
            if self.user_menu_choice == "S":
                self.status = 2
                self.run_game()
            elif self.user_menu_choice == "D":
                self.status = 1
                self.difficulty = self.choose_difficulty()
            elif self.user_menu_choice == "A":
                self.status = 1
                print(self.display_about())
            elif self.user_menu_choice == "Q":
                confirmed = self.confirm_quit()
                if confirmed:
                    print("GOODBYE!\n")
                    self.status = 4
            else:
                print("This option is not valid")
                chosen = False
            chosen = True
        return
