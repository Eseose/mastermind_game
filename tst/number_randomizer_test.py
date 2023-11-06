import unittest
from src.number_randomizer import NumberRandomizer
from unittest.mock import Mock, patch


class NumberRandomizerTest(unittest.TestCase):

    def test_init(self):
        randomizer = NumberRandomizer(maximum=9)

        self.assertEqual(randomizer.maximum, 9,
                         "Number Randomizer class fails to set maximum numbers parameter.")
        self.assertEqual(randomizer.length, 4,
                         "Number Randomizer class fails to set default length parameter.")

    def test_numberRandomizer_maxParam(self):
        randomizer = NumberRandomizer(maximum=9)
        with patch("src.number_randomizer.NumberRandomizer.get") as get:
            get.return_value = "0123456789"
            result = randomizer.get(rtype=str)
        self.assertNotEqual(
            result, None, "Number Randomizer class unexpectedly returned None")
        self.assertNotEqual(
            type(result), tuple, "Number Randomizer API unexpectedly fails")
        self.assertEqual(
            len(result), 10, "Number Randomizer class fails to retrieve correct maximum parameter")
