import unittest
import a3

class TestA3(unittest.TestCase):

    def test_is_valid_word(self):
        self.assertEqual(a3.is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO'), True)
        self.assertEqual(a3.is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'AR'), False)
        self.assertEqual(a3.is_valid_word(['AMERICA', 'ENGLAND', 'UK'], 'MERICA'), False)