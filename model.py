from number_randomizer import NumberRandomizer
from app_config import APP_CONFIG


class GameModel():

    def __init__(self, difficulty):
        self.attempts = 10
        self.attempt = 0
        self.won = False
        self.difficulty = APP_CONFIG.difficulty
        self.num = NumberRandomizer(
            maximum=APP_CONFIG.con["maximum"]).get(r_type=str)
        print("Random Num =", self.num)
