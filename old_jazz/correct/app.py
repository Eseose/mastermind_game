from controller import Controller


# Takes User Input and makes a decision on what view to show. It will also decide what logic to run.
# This is your main_controller
class Game:

    def __init__(self):

        self.game = Controller()
        self.state = self.game.status_msgs

    def run_game(self):
        user_input = None
        while self.state != 4:
            if self.state == 1:
                menu = self.game.choose_menu()
                pass
            elif self.state == 2:
                pass
            elif self.state == 3:
                pass
        return
