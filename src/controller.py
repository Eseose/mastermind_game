from statemachine import StateMachine, State
from collections import Counter
from src.view import Display
from src.model import GameModel, RoundModel
from src.app_config import APP_CONFIG, DifficultyConfigDefault
import time


class GameControl(StateMachine):
    "A MASTERMIND Game"
    on = State(initial=True)  # started
    # settings = State()  # oversabi ooo trying to factor in back to main menu
    in_progress = State()
    finished = State()
    off = State(final=True)  # exited

    choose_difficulty = on.to(on, on="difficulty_chosen")
    initialize_game = on.to(in_progress, on="game_initialized")
    make_attempt = (
        in_progress.to(in_progress, unless="game_finished") |
        in_progress.to(finished, cond="game_finished")
    )
    restart_game = finished.to(on)

    exit_to_main_menu = (
        on.to(on) |
        in_progress.to(on) |
        finished.to(on)
    )

    quit_game = (
        on.to(off, cond="action_confirmed") |
        on.to(on, unless="action_confirmed") |
        in_progress.to(off, cond="action_confirmed") |
        in_progress.to(in_progress, unless="action_confirmed") |
        finished.to(off, cond="action_confirmed") |
        finished.to(finished, unless="action_confirmed")
    )

    def __init__(self):

        self.game_model = None
        self.guess = None
        self.start_time = None
        self.correct_nums = None
        self.correct_loc = None
        self.result = None

        self.view = Display()

        super(GameControl, self).__init__()

    def game_finished(self, guess):
        self.guess = guess
        if guess == self.game_model.num:
            self.game_model.won = True
            return True

        attempts_left = self.game_model.attempts - self.game_model.attempt - 1
        if attempts_left == 0:
            self.game_model.won = False
            return True
        return False

    def on_enter_finished(self):
        # Player quit game.
        if self.game_model.won is None:
            return
        # Player finished game
        stop_time = time.time()
        self.game_model.time_elapsed = stop_time - self.start_time
        session = APP_CONFIG.get_db_session()
        session.add_all([self.game_model])
        session.commit()

    def check_precision(self, guess):
        correct_nums, correct_loc = 0, 0
        num_freq = Counter(self.game_model.num)
        for i in range(len(guess)):
            if guess[i] == self.game_model.num[i]:
                correct_loc += 1
            if guess[i] in num_freq and num_freq[guess[i]] != 0:
                correct_nums += 1
                num_freq[guess[i]] -= 1
        if correct_nums == 0 and correct_loc == 0:
            self.result = "All Incorrect"
        elif correct_nums == 4 and correct_loc == 4:
            self.result = "All Correct"
        else:
            self.result = "Partial"
        self.correct_nums = correct_nums
        self.correct_loc = correct_loc

    def after_make_attempt(self):
        self.check_precision(self.guess)

        # Record Game Round Data
        round_model = RoundModel(
            self.game_model.game_id,
            self.game_model.attempt,
            self.guess,
            self.correct_nums,
            self.correct_loc,
            self.result
        )
        self.game_model.rounds.append(round_model)
        APP_CONFIG.get_db_session().add_all([round_model])
        APP_CONFIG.get_db_session().commit()
        self.display_attempt_result()
        self.game_model.attempt += 1

    def display_attempt_result(self):
        if self.game_model.won:
            self.view.display_winner(
                num=self.game_model.num, attempt=self.game_model.attempt)
        else:
            if self.game_model.attempt == 10:
                self.view.display_loser(num=self.game_model.num)
            elif self.correct_nums == 0 and self.correct_loc == 0:
                self.view.display_incorrect()
            else:
                self.view.display_incorrect(
                    correct_nums=self.correct_nums, correct_loc=self.correct_loc)

    def game_initialized(self):
        # sets game(i.e attempts, difficulty, num)based on user_setting or default
        self.start_time = time.time()
        self.game_model = GameModel()
        APP_CONFIG.get_db_session().add_all([self.game_model])
        APP_CONFIG.get_db_session().commit()
        APP_CONFIG.current_game_id = self.game_model.game_id

    def difficulty_chosen(self, choice):
        APP_CONFIG.set_difficulty(
            list(DifficultyConfigDefault.keys())[choice - 1])
        if APP_CONFIG.difficulty is not None:
            return True
        return False

    def action_confirmed(self, choice):
        if choice == "Y":
            return True
        return False
