from controller import Controller


class View:

    def __init__(self):
        # Can Be ENUMS
        self.status_msgs = {1: "ON",
                            2: "IN PROGRESS",
                            3: "FINISHED",
                            4: "OFF"}

        # Can Be ENUMS
        self.difficulty_levels = {1: "Easy",
                                  2: "Medium",
                                  3: "Hard"}

        self.menu_choices = {"S": "Start",
                             "D": "Difficulty",
                             "A": "About",
                             "Q": "Quit"}
        self.status = None
        self.difficulty = None
        self.main_menu = None
        self.game = None
        self.user_menu_choice = None
        self.previous_menu_choice = None
        self.menu_change = None

    def initialize_game(self):
        self.status = 1
        self.game = Controller()
        self.difficulty = self.difficulty_levels[2]
        self.main_menu = self.generate_menu()
        print(self.main_menu)
        return self.detect_menu_choice()

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

    def get_menu_choice_int(self):
        try:
            user_choice = int(input("Choose Option Number: "))
        except:
            print("Please choose the option number (e.g 1)")
            self.get_menu_choice()  # something better than recursion
        return user_choice

    def get_menu_choice_str(self):
        valid = False
        while not valid:
            user_choice = input("Main Menu Choice: ").upper()
            if user_choice in self.menu_choices:
                valid = True
            else:
                print("Please choose the option alphabet (e.g S)")
        return user_choice

    def get_yes_or_no_choice(self, msg):
        options = {"Y": "Yes",
                   "N": "No"}
        user_choice = None
        new_msg = msg + str(options).strip("{}").replace(", ", "\n")
        while user_choice not in options:
            user_choice = input(f"{new_msg}\nYour Choice: ").upper()
        return user_choice

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

    def confirm_quit(self):
        choice = self.get_yes_or_no_choice(msg="Quit Game?\n")
        if choice == "Y":
            return True
        return False

    def display_about(self):
        about = "\t\tABOUT\n"
        about_1 = "Your task is to guess a 4 digit number correctly "
        about_2 = "from a total of 8 different numbers.\nThe number "
        about_3 = "of attempts you have depends on your choosen "
        about_4 = "difficulty level.\nPossible Numbers: [0  1  2  3  4  5  6  7]"
        about_5 = "\nGOOD LUCK!\n"
        about_msg = about + about_1 + about_2 + about_3 + about_4 + about_5
        return about_msg

    def display_difficulty(self):
        difficulty_levels_str = str(self.difficulty_levels).strip(
            "{}").replace(", ", "\n")
        display = (f"Difficulty Levels:\n{difficulty_levels_str}\n")
        return display

    def choose_difficulty(self):
        display = self.display_difficulty()
        print(display)
        user_choice = self.get_menu_choice_int()
        if 0 < user_choice < 4:
            self.difficulty = self.difficulty_levels[user_choice]
        else:
            options = str(self.difficulty_levels.keys()).replace(
                "dict_keys", "").strip("()")
            print(f"Choose a valid option from {options}")
        return

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

    def run_game(self):
        game_initialized, game_msg = self.game.initialize_game(
            difficulty=self.difficulty)
        attempts = self.game.attempts
        if game_initialized:
            intro_0 = "Guess a four digit number made up of "
            intro_1 = "only numbers between 0 and 7 inclusive.\n"
            intro_2 = f"You have ONLY {attempts} attempts.\n"
            intro = intro_0 + intro_1 + intro_2
            print(intro)
            for attempt in range(attempts):
                guess = self.get_user_guess(
                    attempt=attempt, attempts=attempts)
                correct_guess = self.game.validate_guess(guess=guess)
                if correct_guess:
                    print("All correct. You are a mastermind!")
                    return
                else:
                    correct_nums, correct_loc = self.game.check_precision(
                        guess=guess)
                if correct_nums == 0:
                    print("all incorrect")
                else:
                    print(f"{correct_nums} correct number and "
                          f"{correct_loc} correct location")

            print("You ran out of attempts, you lose!")
        else:
            print(game_msg)  # error
        return

    def get_user_guess(self, attempt, attempts):
        valid_input = False
        while not valid_input:
            msg = f"You have {attempts - attempt} attempts left.\n"
            guess_str = input(f"{msg}Round{attempt + 1}\nYour Guess?... \n")
            is_valid = self.is_valid(guess_str=guess_str)
            if is_valid[0]:
                valid_input = True
                guess = [int(item) for item in guess_str]
                return guess
            else:
                print(is_valid[1])

    def is_valid(self, guess_str) -> tuple:
        try:
            guess_int = int(guess_str)
        except:
            return (False, "Please input must be numbers.")
        count = 4
        for char in guess_str:
            if 0 <= int(char) < 8:
                count -= 1
        if count == 0:
            return (True, )
        else:
            return (False, "The 4 numbers in your guess must ONLY"
                    " be chosen from these [0, 1, 2, 3, 4, 5, 6, 7]")


test = View()
test.initialize_game()
