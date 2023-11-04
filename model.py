from number_randomizer import NumberRandomizer
from app_config import APP_CONFIG


class GameModel():

    def __init__(self):
        self.attempts = APP_CONFIG.config["attempts"]
        self.attempt = 0
        self.won = False
        self.difficulty = APP_CONFIG.difficulty
        self.num = NumberRandomizer(
            maximum=APP_CONFIG.config["maximum"]).get(r_type=str)
        print("Random Num =", self.num)
