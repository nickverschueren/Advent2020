import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def test_part1a(self):
        numbers = readInput('testinput.txt')
        actual = part1(numbers)
        self.assertEqual(436, actual)

    def test_part1b(self):
        numbers = readInput('testinput2.txt')
        actual = part1(numbers)
        self.assertEqual(1, actual)

    def test_part2a(self):
        numbers = readInput('testinput.txt')
        actual = part2(numbers)
        self.assertEqual(175594, actual)

    def test_part2b(self):
        numbers = readInput('testinput2.txt')
        actual = part2(numbers)
        self.assertEqual(2578, actual)

if __name__ == '__main__':
    unittest.main()
