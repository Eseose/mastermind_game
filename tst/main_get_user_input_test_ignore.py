from src.controller import GameControl
from src.view import Display
from main import get_user_input
import unittest
from unittest.mock import Mock, patch


class MainGetUserInputTest(unittest.TestCase):

    def setUp(self):
        self.game = GameControl()
        self.view = Display()

        self.addClassCleanup(patch.stopall)

    def tearDown(self):
        self.addClassCleanup(patch.stopall)

    # Runs the whole State Machine
    # def test_getUserInput_onState_mainMenu(self):
    #     self.game.current_state = self.game.on
    #     with patch("src.view.Display.display_main_menu") as display:
    #         display.return_value = "Main Menu"
    #         menu = self.get_user_input(self.game, self.view)
    #     self.assertNotEqual(
    #         menu, None, "Main Get User Input unexpectedly returned None")
    #     self.assertEqual(
    #         menu, "Main Menu", "Main Get User Input fails to display correct menu")
