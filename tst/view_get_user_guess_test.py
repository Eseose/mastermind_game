import unittest
from src.view import Display
from unittest.mock import Mock, patch


class viewDisplayGetUserGuessTest(unittest.TestCase):

    def setUp(self):
        self.display = Display()

        self.addClassCleanup(patch.stopall)

    def tearDown(self):
        self.addClassCleanup(patch.stopall)

    def test_getUserGuess_validqInput(self):
        with patch("builtins.input") as _input:
            _input.return_value = "q"
            result = self.display.get_user_guess(attempt=1)
        self.assertNotEqual(
            result, None, "Get_User_Guess function unexpectedly returned None")
        self.assertEqual(
            result, "Q", "Get_User_Guess function fails to accept Quit as valid or "
            "fails to convert lowercase 'q' to uppercase 'Q'")

    def test_getUserGuess_validInput(self):
        with patch("builtins.input") as _input, \
                patch("src.view.Display.is_valid") as _is_valid:
            _input.return_value = "1234"
            _is_valid.return_value = (True, )
            result = self.display.get_user_guess(attempt=1)
        self.assertNotEqual(
            result, None, "Get_User_Guess function unexpectedly returned None")
        self.assertEqual(
            result, "1234", "Get_User_Guess function fails to return a valid guess.")

    # Test infinite while loop created by get_user_guess
