from src.number_randomizer import NumberRandomizer
from src.app_config import APP_CONFIG, Base

from sqlalchemy import Column, Identity, ForeignKey
from sqlalchemy import Integer, Boolean, String, Double


class GameModel(Base):
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

    def __str__(self):
        return f"player: {self.player}\ngame_id: {self.game_id}\nattempt: ({self.attempt + 1}/{self.attempts})\ntime_elapsed: {self.time_elapsed}\ndifficulty: {self.difficulty}"


class RoundModel(Base):
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

    def __str__(self):
        return f"attempt: {self.attempt + 1}\nguess: {self.guess}\nresult: {self.result}\ncorrect_nums: {self.correct_nums}\ncorrect_loc: {self.correct_loc}"
