import unittest
from main import readInput, readInput2, part1, part2

class TestParts(unittest.TestCase):
    def test_part1(self):
        input = readInput('testinput.txt')
        actual = part1(input)
        self.assertEqual(295, actual)

    def test_part2a(self):
        input = readInput2('testinput2.txt')
        actual = part2(input)
        self.assertEqual(3417, actual)

    def test_part2b(self):
        input = readInput2('testinput3.txt')
        actual = part2(input)
        self.assertEqual(754018, actual)

    def test_part2c(self):
        input = readInput2('testinput4.txt')
        actual = part2(input)
        self.assertEqual(779210, actual)

    def test_part2d(self):
        input = readInput2('testinput5.txt')
        actual = part2(input)
        self.assertEqual(1261476, actual)

    def test_part2e(self):
        input = readInput2('testinput6.txt')
        actual = part2(input)
        self.assertEqual(1202161486, actual)

if __name__ == '__main__':
    unittest.main()
