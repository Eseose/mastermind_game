from src.app_config import APP_CONFIG
from src.queries import Queries


class Display:

    def __init__(self):

        self.input = None
        self.output = None

    def get_int(self, options):
        choice_int = None
        while choice_int not in options:
            choice = input("Choose Option Number: ")
            if choice.upper() == "Q":
                return choice.upper()
            else:
                try:
                    choice_int = int(choice)
                except:
                    print("Please choose the option number (e.g 1)")
        return choice_int

    def get_str(self, options):
        choice = None
        while choice not in options:
            choice = input("Your Choice: ").upper()
        return choice.upper()

    def get_user_name(self):
        if APP_CONFIG.current_player is not None:
            return
        APP_CONFIG.current_player = input("Enter Username: ")

    def display_main_menu(self):
        welcome = "\t\tWELCOME TO MASTERMIND\n\n"
        choices = "S : Start\nD : Difficulty\nA : About\nL : Leader Board\nQ : Quit\n"
        menu = welcome + choices
        print(menu)
        return self.get_str(options={"S", "D", "A", "L", "Q"})

    def display_end_menu(self):
        thanks = "\n\tThank you for playing MASTERMIND!!!\n"
        question = "\nWould you like to play again?..\n"
        choices = "R : Restart\nQ : Quit\n"
        menu = thanks + question + choices
        print(menu)
        choice = self.get_str(options={"R", "Q"})
        if choice == "Q":
            APP_CONFIG.current_player = None
        return choice

    def display_confirm_quit(self):
        choice = None
        while choice not in {"Y", "N"}:
            choice = input("Quit Game? [Y/N] ").upper()
        return choice.upper()

    def display_choose_difficulty(self):
        display = "Difficulty Levels:\n1 : Easy\n2 : Medium [DEFAULT]\n3 : Hard\n4 : Exit\n"
        print(display)
        choice = self.get_int(options={1, 2, 3, 4})

        if choice == 4:
            return "Q"
        return choice

    def display_about(self):
        possible_numbers = [i for i in range(APP_CONFIG.config["maximum"] + 1)]
        about_full = f"""
            ABOUT
    Your task is to guess a 4 digit number correctly from a total of {len(possible_numbers)} different numbers.
    The number of attempts you have depends on your choosen difficulty level.
    Possible Numbers: {possible_numbers}
    GOOD LUCK!
        
    """
        print(about_full)
        choice = input("Press ENTER to exit")
        return choice

    def display_leader_board(self):
        print(f"\t\tLEADER BOARD [{APP_CONFIG.difficulty}]\n\n")
        for game_model in Queries.get_leaders():
            print(game_model)
        print("\n")
        choice = input("Press ENTER to exit\n")
        return choice

    def display_rounds(self):
        if APP_CONFIG.current_game_id is not None:
            print(
                f"\n\t\tGUESS HISTORY FOR PLAYER [{APP_CONFIG.current_player}]\n")
            for round_model in Queries.get_rounds():
                print(round_model)
            print("\n")
        # # # If no round has been played in current game
        # else:
        #     print("Guess History Unavailable. START Game.")
        # choice = input("Press ENTER to exit")
        # return choice

    def display_winner(self, num, attempt):
        attempts = APP_CONFIG.config["attempts"]
        print(
            f"\t\tYou are a MASTERMIND!\n\tYou guessed {num} in {attempt + 1} out of {attempts} attempts!")

    def display_loser(self, num):
        print(f"Oops, You ran out of attempts.\nThe correct number is {num}.")

    def display_incorrect(self, correct_nums=None, correct_loc=None):
        if correct_nums is None and correct_loc is None:
            print("All incorrect numbers")
        else:
            print(
                f"Correct numbers: {correct_nums}\nCorrect locations: {correct_loc}\n")

    def get_user_guess(self, attempt):
        attempts = APP_CONFIG.config["attempts"]
        valid_input = False
        while not valid_input:
            msg = (f"You have {attempts - attempt} attempts left.\n")
            # "Enter G to view your previous guesses\n")
            self.display_rounds()
            guess_str = input(f"{msg}Round{attempt + 1}\nYour Guess?... \n")
            if guess_str.upper() == "Q":
                valid_input = True
                return guess_str.upper()
            elif guess_str.upper == "G":
                valid_input = True
                return guess_str.upper()
            else:
                is_valid = self.is_valid(guess_str=guess_str)
                if is_valid[0]:
                    valid_input = True
                    # guess = [int(item) for item in guess_str]
                    return guess_str
                else:
                    print(is_valid[1])

    def is_valid(self, guess_str) -> tuple:
        maximum = APP_CONFIG.config["maximum"]
        possible_numbers = [i for i in range(APP_CONFIG.config["maximum"] + 1)]
        try:
            guess_int = int(guess_str)
        except:
            return (False, "Please input must be numbers.")
        count = 4
        for char in guess_str:
            if 0 <= int(char) < maximum + 1:
                count -= 1
        if count == 0:
            return (True, )
        else:
            return (False, "The 4 numbers in your guess must ONLY"
                    f" be chosen from these {possible_numbers}")

    def display_msg(self, msg):
        print(msg)
