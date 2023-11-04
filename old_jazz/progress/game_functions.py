from number_randomizer import NumberRandomizer
from collections import Counter


class StartGame:
    def __init__(self):
        self.num = self.get_random_num()
        self.attempts = 10
        self.guess = None

        self.initialize_game()

    def initialize_game(self):
        for attempt in range(self.attempts):
            self.guess = self.get_user_input(attempt=attempt)
            correct_nums, correct_loc = 0, 0
            num_freq = Counter(self.num)
            if self.guess == self.num:
                print("All correct. You are a mastermind!")
                return
            else:
                for i in range(len(self.guess)):
                    if self.guess[i] == self.num[i]:
                        correct_nums += 1
                        correct_loc += 1
                    else:
                        if self.guess[i] in num_freq and num_freq[self.guess[i]] != 0:
                            correct_nums += 1
                            num_freq[self.guess[i]] -= 1
                if correct_nums == 0:
                    print("all incorrect")
                else:
                    print(f"{correct_nums} correct number and"
                          f" {correct_loc} correct location")

        print("You ran out of attempts, you lose!")
        return

    def get_random_num(self):
        generator = NumberRandomizer()
        num = generator.get()
        print("Generated Number:", num)
        return num

    def get_user_input(self, attempt):
        valid_input = False
        while not valid_input:
            guess_str = input("Guess a four digit number made up of "
                              "only numbers between 0 and 7 inclusive.\n"
                              f"You have {self.attempts - attempt} attempts.\n"
                              "Your Guess?... \n")
            is_valid = self.is_valid(guess_str)
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
            return (False, "4 numbers must ONLY be chosen from these [0, 1, 2, 3, 4, 5, 6, 7]")


game_start = StartGame()
