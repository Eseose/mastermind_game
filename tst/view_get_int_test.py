import unittest
from view import Display


class viewDisplayGetIntTest(unittest.TestCase):

    def setUp(self):
        self.display = Display()

        self.addClassCleanup(patch.stopall)

    def tearDown(self):
        self.addClassCleanup(patch.stopall)

    def test_getInt_validIntInput(self):
        options = {1, 2, 3}
        with patch("view.display.input") as _input:
            _input.return_value = "2"
            result = self.display.get_int(options)
        self.assertNotEqual(
            result, None, "Get_Int function unexpectedly returned None")
        self.assertEqual(
            result, 2, "Get_Int function fails to convert input to integer")

    def test_getInt_validLowercaseQInput(self):
        options = {1, 2, 3}
        with patch("view.display.input") as _input:
            _input.return_value = "q"
            result = self.display.get_int(options)
        self.assertNotEqual(
            result, None, "Get_Int function unexpectedly returned None")
        self.assertEqual(
            result, "Q", "Get_Int function fails to convert lowercase 'q' to uppercase 'Q'")

    def test_getInt_invalidInput_unexpectedError(self):
        options = {1, 2, 3}
        with patch("view.display.input") as _input:
            _input.return_value = "s"
            with self.assertRaises(ValueError):
                result = self.display.get_int(options)
            try:
                result = self.display.get_int(options)
            except ValueError as ex:
                error = "Please choose the option number (e.g 1)"
                self.assertEqual(
                    ex, error, "Get_Int function fails to throw ValueError Exception for input not integer or 'Q'")

    def test_getInt_validQInput_unexpectedError(self):
        options = {1, 2, 3}
        with patch("view.display.input") as _input:
            _input.return_value = "q"
            with self.assertRaises(ValueError):
                result = self.display.get_int(options)
            try:
                result = self.display.get_int(options)
            except ValueError as ex:
                error = "Please choose the option number (e.g 1)"
                self.assertNotEqual(
                    ex, error, "Get_Int function incorrectly throws ValueError Exception for input 'q' and 'Q'")

    # function that tests the while input loop
