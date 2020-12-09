import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.numbers = readInput('testinput.txt')

    def test_part1(self):
        actual = part1(self.numbers, 5)
        self.assertEqual((14, 127), actual)

    def test_part2(self):
        actual = part2(self.numbers, 127)
        self.assertEqual(62, actual)

if __name__ == '__main__':
    unittest.main()
