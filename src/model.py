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
    won = Column("won", Boolean, nullable=False)
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
        self.num = NumberRandomizer(
            maximum=APP_CONFIG.config["maximum"]).get(r_type=str)
        print("Random Num =", self.num)

    def __str__(self):
        return f"player: {self.player}\ngame_id: {self.game_id}\nattempt: ({self.attempt + 1}/{self.attempts})\ntime_elapsed: {self.time_elapsed}\ndifficulty: {self.difficulty}"
