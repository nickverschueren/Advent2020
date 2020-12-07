import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def test_part1(self):
        groups = readInput('testinput.txt')
        actual = part1(groups)
        self.assertEqual(4, actual)

    def test_part2a(self):
        groups = readInput('testinput.txt')
        actual = part2(groups)
        self.assertEqual(32, actual)

    def test_part2b(self):
        groups = readInput('testinput2.txt')
        actual = part2(groups)
        self.assertEqual(126, actual)

if __name__ == '__main__':
    unittest.main()