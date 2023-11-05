import unittest
from src.view import Display
from unittest.mock import Mock, patch


class viewDisplayGetIntTest(unittest.TestCase):

    def setUp(self):
        self.display = Display()

        self.addClassCleanup(patch.stopall)

    def tearDown(self):
        self.addClassCleanup(patch.stopall)

    def test_getInt_validIntInput(self):
        options = {1, 2, 3}
        with patch("builtins.input") as _input:
            _input.return_value = "2"
            result = self.display.get_int(options)
        self.assertNotEqual(
            result, None, "Get_Int function unexpectedly returned None")
        self.assertEqual(
            result, 2, "Get_Int function fails to convert input to integer")

    def test_getInt_validQInput(self):
        options = {1, 2, 3}
        with patch("builtins.input") as _input:
            _input.return_value = "q"
            result = self.display.get_int(options)
        self.assertNotEqual(
            result, None, "Get_Int function unexpectedly returned None")
        self.assertEqual(
            result, "Q", "Get_Int function fails to accept 'q' as valid or "
            "fails to convert lowercase 'q' to uppercase 'Q'")

    # # function that tests the infinite while input loop which does NOT allow invalid input
    # def test_getInt_invalidInput(self):
    #     options = {1, 2, 3}
    #     with patch("builtins.input") as _input:
    #         _input.return_value = "s"
    #         result = self.display.get_int(options)
    #         error = "Please choose the option number (e.g 1)"
    #         self.assertEqual(result, error, "Get_Int function fails to print error for"
    #                          "invalid input (not integer in available options or 'Q')")
