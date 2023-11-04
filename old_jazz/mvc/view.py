from controller.game_controller import GameController
from controller.menu_controller import MenuController
# Takes User Input and makes a decision on what view to show. It will also decide what logic to run.
# This is your main_controller


class Game:

    def __init__(self):

        self.game_controller = GameController()
        self.menu_controller = MenuController()
        self.state = self.game.status_msgs

    def run_game(self):
        user_input = None
        while self.state != 4:  # OFF
            if self.state == 1:
                menu = self.menu_controller.choose_menu()
                pass
            elif self.state == 2:
                pass
            elif self.state == 3:
                pass
        return
