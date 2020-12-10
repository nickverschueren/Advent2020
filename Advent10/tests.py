import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def test_part1a(self):
        ratings = readInput('testinput.txt')
        actual = part1(ratings)
        self.assertEqual(35, actual)

    def test_part1b(self):
        ratings = readInput('testinput2.txt')
        actual = part1(ratings)
        self.assertEqual(220, actual)

    def test_part2a(self):
        ratings = readInput('testinput.txt')
        actual = part2(ratings)
        self.assertEqual(8, actual)

    def test_part2b(self):
        ratings = readInput('testinput2.txt')
        actual = part2(ratings)
        self.assertEqual(19208, actual)

if __name__ == '__main__':
    unittest.main()
