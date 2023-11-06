from src.number_randomizer import NumberRandomizer
from src.app_config import APP_CONFIG, Base

from sqlalchemy import Column, Identity, ForeignKey
from sqlalchemy import Integer, Boolean, String, Double


class GameModel(Base):

    r'''
        Creates a table named "games" in the SQL database.

        Database Table Columns
        :param game_id: stores unique game_id, Integer, Identity(), primary_key=True
        :param attempts: total number of attempts in game, Integer, nullable=False)
        :param attempt: last attempt when game was completed, Integer, nullable=False)
        :param time_elapsed: time taken to make a guess, Double, nullable=True)
        :param won: is game won, lost or None(initial/quit), Boolean, nullable=True)
        :param difficulty: level of game difficulty, String, nullable=False)
        :param num: random number to be guessed, String, nullable=False)
        :param player: username of player, String, nullable=False)

    '''

    __tablename__ = "games"

    # Database Table Fields
    game_id = Column("game_id", Integer, Identity(), primary_key=True)
    attempts = Column("attempts", Integer, nullable=False)
    attempt = Column("attempt", Integer, nullable=False)
    time_elapsed = Column("time_elapsed", Double, nullable=True)
    won = Column("won", Boolean, nullable=True)
    difficulty = Column("difficulty", String, nullable=False)
    num = Column("num", String, nullable=False)
    player = Column("player", String, nullable=False)

    def __init__(self):
        self.attempts = APP_CONFIG.config["attempts"]
        self.attempt = 0
        self.time_elapsed = None
        self.won = None
        self.difficulty = APP_CONFIG.difficulty
        self.player = APP_CONFIG.current_player
        self.rounds = []
        self.num = NumberRandomizer(
            maximum=APP_CONFIG.config["maximum"]).get(r_type=str)
        print("Random Num =", self.num)

    # string representation of GameModel object
    def __str__(self):
        return f"player: {self.player}, attempt: ({self.attempt + 1}/{self.attempts}), time_elapsed: {self.time_elapsed}"


class RoundModel(Base):

    r'''
        Creates a table named "rounds" in the SQL database.

        Database Table Columns
        :param round_id: stores unique round_id, Integer, Identity(), primary_key=True
        :param game_id: stores game_id from games table, Integer, ForeignKey=True
        :param attempt: current attempt being played, Integer, nullable=False)
        :param guess: current guess made, String, nullable=False)
        :param correct_nums: number of correct digits in guess, Integer, nullable=False)
        :param correct_loc: number of correct digit locations in guess, Integer, nullable=False)

    '''
    __tablename__ = "rounds"

    # Database Table Fields
    round_id = Column("round_id", Integer, Identity(), primary_key=True)
    game_id = Column("game_id", Integer, ForeignKey(GameModel.game_id))
    attempt = Column("attempt", Integer, nullable=False)
    guess = Column("guess", String, nullable=False)
    correct_nums = Column("correct_nums", Integer, nullable=False)
    correct_loc = Column("correct_loc", Integer, nullable=False)
    result = Column("result", String, nullable=False)

    def __init__(self, game_id, attempt, guess, correct_nums, correct_loc, result):
        self.game_id = game_id
        self.attempt = attempt
        self.guess = guess
        self.correct_nums = correct_nums
        self.correct_loc = correct_loc
        self.result = result

    # string representation of RoundModel object
    def __str__(self):
        return f"attempt: {self.attempt + 1}, guess: {self.guess}, result: {self.result}, correct_nums: {self.correct_nums}, correct_loc: {self.correct_loc}"
