import unittest
from main import readInput, part1#, part2

class TestParts(unittest.TestCase):
    def test_part1a(self):
        input = readInput('testinput.txt')
        actual = part1(input)
        self.assertEqual(71, actual)

if __name__ == '__main__':
    unittest.main()
