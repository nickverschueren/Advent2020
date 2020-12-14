import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def test_part1(self):
        program = readInput('testinput.txt')
        actual = part1(program)
        self.assertEqual(165, actual)

    def test_part2(self):
        program = readInput('testinput2.txt')
        actual = part2(program)
        self.assertEqual(208, actual)

if __name__ == '__main__':
    unittest.main()
