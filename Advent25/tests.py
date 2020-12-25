import unittest
from main import part1

class TestParts(unittest.TestCase):
    def test_part1(self):
        actual = part1(5764801, 17807724)
        self.assertEqual(14897079, actual)

if __name__ == '__main__':
    unittest.main()
