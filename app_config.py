DifficultyConfigDefault = {
    "Easy": {
        "maximum": 5
    },
    "Medium": {
        "maximum": 7
    },
    "Hard": {
        "maximum": 9
    }
}


class AppConfig:

    def __init__(self):
        self.difficulty = "Medium"
        self.config = {}
        self.set_difficulty(difficulty)

    def set_difficulty(self, difficulty):
        if difficulty not in DifficultyConfigDefault:
            return False
        self.difficulty = difficulty
        self.config = DifficultyConfigDefault[difficulty]


APP_CONFIG = AppConfig()
