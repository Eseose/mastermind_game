import unittest
from statemachine import StateMachine, State
from collections import Counter
from src.controller import GameControl
from src.model import GameModel
from unittest.mock import Mock, patch


class controllerGameControlCheckPrecisionTest(unittest.TestCase):

    def setUp(self):
        self.game = GameControl()
        self.game.result = None
        self.game.correct_loc = None
        self.game.correct_nums = None

        self.addClassCleanup(patch.stopall)

    def tearDown(self):
        self.addClassCleanup(patch.stopall)

    def test_checkPrecision_resultAllCorrect(self):
        with patch("src.controller.GameControl.game_model.num") as game_model_num:
            game_model_num.return_value = "1234"
            self.game.check_precision(guess="1234")
        self.assertNotEqual(
            result, None, "Check Precision function unexpectedly returned None")
        self.assertEqual(self.game.result, "All correct",
                         "Check Precision function fails to correctly set member variable")
