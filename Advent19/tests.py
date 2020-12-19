import unittest
from main import readInput, part1, part1b, part2

class TestParts(unittest.TestCase):
    def test_part1(self):
        input = readInput('testinput.txt')
        actual = part1(input)
        self.assertEqual(2, actual)

    def test_part1b(self):
        input = readInput('testinput.txt')
        actual = part1b(input)
        self.assertEqual(2, actual)

    def test_part2(self):
        input = readInput('testinput2.txt')
        actual = part2(input)
        self.assertEqual(12, actual)

if __name__ == '__main__':
    unittest.main()
