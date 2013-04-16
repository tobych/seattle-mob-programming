import unittest
import hashlib
from comparer import *

class ComparerTest(unittest.TestCase):

    def test_compareTwoValues(self):
        unit = Comparer('a', 'a')
        self.assertEqual(True, unit.compareTwoHashCodes())

    def test_generateHash(self):
        unit = HashGenerator('foo')
        actual_value = unit.doHash()
        expected_value = hashlib.md5('foo').hexdigest()

        self.assertEqual(actual_value, expected_value)

if __name__ == '__main__':
    unittest.main()


