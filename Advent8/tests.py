import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.program = readInput('testinput.txt')

    def test_part1(self):
        actual = part1(self.program)
        self.assertEqual(5, actual)

    def test_part2(self):
        actual = part2(self.program)
        self.assertEqual(8, actual)

if __name__ == '__main__':
    unittest.main()
