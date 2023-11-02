from number_randomizer import NumberRandomizer
from statemachine import StateMachine, State
from collections import Counter
from view import Display


class GameControl(StateMachine):
    "A MASTERMIND Game"
    on = State(initial=True)  # started
    # settings = State()  # oversabi ooo trying to factor in back to main menu
    in_progress = State()
    finished = State()
    off = State(final=True)  # exited

    choose_difficulty = on.to(on, on="difficulty_chosen")
    about = on.to(on, on="exit_about")
    initialize_game = on.to(in_progress, on="game_initialized")
    make_attempt = (
        in_progress.to(in_progress, unless="game_finished") |
        in_progress.to(finished, cond="game_finished")
    )
    restart_game = finished.to(on)
# ---------------------------------------------------------------------------------------------- #
    # neater way needed (on,in_prog,off).to(off, cond="quit_confirmed")
    # | (on,in_prog,off).to.itself(unless="quit_confirmed")

    quit_game = ((
        on.to(off, cond="quit_confirmed") | on.to(
            on, unless="quit_confirmed")) | (
        in_progress.to(off, cond="quit_confirmed") | in_progress.to(
            in_progress, unless="quit_confirmed")) | (
        finished.to(off, cond="quit_confirmed") | finished.to(
            finished, unless="quit_confirmed"))
    )

    # quit_game_menu = on.to(off, cond="quit_confirmed") | on.to(
    #     on, unless="quit_confirmed")

    # quit_game_playing = in_progress.to(off, cond="quit_confirmed") | in_progress.to(
    #     in_progress, unless="quit_confirmed")

    # quit_game_finished = finished.to(off, cond="quit_confirmed") | finished.to(
    #     finished, unless="quit_confirmed")

    def __init__(self):

        self.num = None
        self.attempts = None
        self.attempt = None
        self.guess = None
        self.won = None
        self.difficulty = None  # set at game_initiate
        self.difficulty_levels = ["Easy", "Medium", "Hard"]

        self.view = Display()

        super(GameControl, self).__init__()

    def game_finished(self, guess):
        self.guess = guess
        if guess == self.num:
            self.won = True
            return True

        attempts_left = self.attempts - self.attempt - 1
        self.attempt += 1
        if attempts_left == 0:
            return True
        return False

    def after_make_attempt(self):
        self.check_precision(self.guess)

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
        if self.won:
            self.view.display_winner(
                num=self.num, attempt=self.attempt, attempts=self.attempts)
        else:
            if self.attempt == 10:
                self.view.display_loser(num=self.num)
            elif correct_nums == 0 and correct_loc == 0:
                self.view.display_incorrect()
            else:
                self.view.display_incorrect(
                    correct_nums=correct_nums, correct_loc=correct_loc)

    def game_initialized(self):
        # sets game(i.e attempts, difficulty, num)based on user_setting or default
        if self.difficulty is None or self.difficulty == "Medium":
            self.difficulty = "Medium"
            self.attempts = 10
        else:
            self.attempts = [5 if difficulty == "Hard" else 15]
        self.won = False
        self.attempt = 0

        self.num = NumberRandomizer().get(r_type=str)
        print(self.num)

    def result_reveal(self):
        if self.won:
            view.display_winner(
                num=self.num, attempt=self.attempt, attempts=self.attempts)
        else:
            if self.attempt == 10:
                view.display_loser(self.num)
            elif self.correct_nums == 0 and self.correct_loc == 0:
                view.display_incorrect(all_incorrect=True)
            else:
                view.display_incorrect(self.correct_nums, self.correct_loc)

    def difficulty_chosen(self, choice):
        self.difficulty = self.difficulty_levels[choice - 1]
        if self.difficulty is not None:
            return True
        return False

    def exit_about(self, choice):
        if choice == "Y":
            return True
        return False

    def quit_confirmed(self, choice):
        if choice == "Y":
            return True
        return False