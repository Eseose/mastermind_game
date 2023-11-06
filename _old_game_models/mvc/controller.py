from number_randomizer import NumberRandomizer
from collections import Counter


class Controller:

    def __init__(self):

        self.num = None
        self.attempts = None

        self.status_msgs = {1: "ON",
                            2: "IN PROGRESS",
                            3: "FINISHED",
                            4: "OFF"}

    def initialize_game(self, difficulty):
        if difficulty == "Medium":
            self.attempts = 10
        else:
            return (False, "implement other difficulties")
        self.num = self.get_random_num()
        return (True, self.num)

    def get_random_num(self):
        generator = NumberRandomizer()
        num = generator.get()
        print("Generated Number:", num)
        return num

    def choose_menu():

        pass

    def run_game(self):
        game_initialized, game_msg = self.game.initialize_game(
            difficulty=self.difficulty)
        attempts = self.attempts
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

    def validate_guess(self, guess):
        if guess == self.num:
            return True
        return False

    def check_precision(self, guess):
        correct_nums, correct_loc = 0, 0
        num_freq = Counter(self.num)
        for i in range(len(guess)):
            if guess[i] == self.num[i]:
                correct_nums += 1
                correct_loc += 1
            else:
                if guess[i] in num_freq and num_freq[guess[i]] != 0:
                    correct_nums += 1
                    num_freq[guess[i]] -= 1
        return correct_nums, correct_loc
