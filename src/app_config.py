from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


DifficultyConfigDefault = {
    "Easy": {
        "maximum": 5,
        "attempts": 10
    },
    "Medium": {
        "maximum": 7,
        "attempts": 10
    },
    "Hard": {
        "maximum": 9,
        "attempts": 10
    }
}


class AppConfig:

    def __init__(self):
        self.difficulty = "Medium"
        self.database_path = "./data/mastermind.db"
        self.config = {}
        self.set_difficulty(self.difficulty)
        self._db_session = None
        self.current_player = None
        self.current_game_id = None

    def set_difficulty(self, difficulty):
        if difficulty not in DifficultyConfigDefault:
            return False
        self.difficulty = difficulty
        self.config = DifficultyConfigDefault[difficulty]

    def get_db_session(self):
        if self._db_session is None:
            engine = create_engine(
                f"sqlite:///{self.database_path}", echo=False)
            Base.metadata.create_all(engine)
            self._db_session = sessionmaker(engine)()
        return self._db_session


APP_CONFIG = AppConfig()
