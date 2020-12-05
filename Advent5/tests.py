import unittest
from main import binaryCountStr

class TestBinaryCountStr(unittest.TestCase):        
    def test_binaryCountStr1(self):
        actual = binaryCountStr('BFFFBBFRRR','BR')
        expected = 567
        self.assertEqual(expected, actual)

    def test_binaryCountStr2(self):
        actual = binaryCountStr('FFFBBBFRRR','BR')
        expected = 119
        self.assertEqual(expected, actual)

    def test_binaryCountStr3(self):
        actual = binaryCountStr('BBFFBBFRLL','BR')
        expected = 820
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()