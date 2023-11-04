import unittest
from src.number_randomizer import NumberRandomizer
import response


class NumberRandomizerGetTest(unittest.TestCase):

    def setUp(self):
        self.number_randomizer = NumberRandomizer()

    self.addClassCleanup(patch.stopall)

    def tearDown(self):
        self.addClassCleanup(patch.stopall)

    def test_get_defaultInput_returnsList(self):
        # mock requests.get() function
        mock_response = unittest.mock.Mock()
        mock_response.status_code
        pass
