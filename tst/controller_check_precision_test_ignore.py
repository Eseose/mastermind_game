import unittest
from src.controller import GameControl
from unittest.mock import Mock, patch


class controllerGameControlCheckPrecisionTest(unittest.TestCase):

    def setUp(self):
        self.game = GameControl()
        self.game_model.num = "1234"
        self.game.result = None
        self.game.correct_loc = None
        self.game.correct_nums = None

        self.addClassCleanup(patch.stopall)

    def tearDown(self):
        self.addClassCleanup(patch.stopall)

    def test_checkPrecision_resultAllCorrect(self):
        self.game.check_precision(guess="1234")
        self.assertNotEqual(
            result, None, "Check Precision function unexpectedly returned None")
        self.assertEqual(self.game.result, "All correct",
                         "Check Precision function fails to correctly set member variable")
