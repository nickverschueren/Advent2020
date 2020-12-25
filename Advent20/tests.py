import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def test_part1(self):
        input = readInput('testinput.txt')
        actual = part1(input)
        self.assertEqual(20899048083289, actual)

    def test_part2(self):
        input = readInput('testinput.txt')
        actual = part2(input)
        self.assertEqual(273, actual)

if __name__ == '__main__':
    unittest.main()
