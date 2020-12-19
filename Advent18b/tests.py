import unittest
from main import part1, part2

class TestParts(unittest.TestCase):
    def test_part1(self):
        actual = part1('testinput.txt')
        self.assertEqual(26335, actual)

    def test_part2(self):
        actual = part2('testinput2.txt')
        self.assertEqual(693942, actual)

if __name__ == '__main__':
    unittest.main()
