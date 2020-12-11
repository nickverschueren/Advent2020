import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def test_part1(self):
        rows = readInput('testinput.txt')
        actual = part1(rows)
        self.assertEqual(37, actual)

    def test_part2(self):
        rows = readInput('testinput.txt')
        actual = part2(rows)
        self.assertEqual(26, actual)

if __name__ == '__main__':
    unittest.main()
