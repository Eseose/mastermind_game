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
        self.config = {}
        self.set_difficulty(self.difficulty)

    def set_difficulty(self, difficulty):
        if difficulty not in DifficultyConfigDefault:
            return False
        self.difficulty = difficulty
        self.config = DifficultyConfigDefault[difficulty]


APP_CONFIG = AppConfig()
