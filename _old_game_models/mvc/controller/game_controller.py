class GameController:

    def __init__(self):
        self.num = None
        self.attempts = None

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
