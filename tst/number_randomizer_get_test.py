import unittest
from src.number_randomizer import NumberRandomizer
from unittest.mock import Mock, patch


class NumberRandomizerGetTest(unittest.TestCase):

    def setUp(self):
        self.generator = NumberRandomizer()

        self.addClassCleanup(patch.stopall)

    def tearDown(self):
        self.addClassCleanup(patch.stopall)

    def test_get_returnsString(self):
        result = self.generator.get(r_type=str)
        result_type = type(result)
        self.assertNotEqual(
            result, None, "Get function unexpectedly returned None")
        self.assertEqual(result_type, str,
                         "Get function fails to return string.")

    def test_get_defaultInput_returnsList(self):
        result = self.generator.get()
        result_type = type(result)
        self.assertNotEqual(
            result, None, "Get function unexpectedly returned None")
        self.assertEqual(result_type, list,
                         "Get function fails to return list.")

    def test_get_defaultInput_returns4Numbers(self):
        result = self.generator.get()
        length = len(result)
        self.assertNotEqual(
            result, None, "Get function unexpectedly returned None")
        self.assertEqual(length, 4,
                         "Get function fails to return 4 digits as default.")
