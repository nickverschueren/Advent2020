import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def test_part1(self):
        input = readInput('testinput.txt')
        actual = part1(input)
        self.assertEqual(26335, actual)

    def test_part2(self):
        input = readInput('testinput2.txt')
        actual = part2(input)
        self.assertEqual(693942, actual)

    def test_evaluate2(self):
        input = list()
        input.append(list('( ( 2 + 4 * 9 ) * ( 6 + 9 * 8 + 6 ) + 6 ) + 2 + 4 * 2'.split(' ')))
        actual = part2(input)
        self.assertEqual(23340, actual)

    def test_evaluate2b(self):
        input = list()
        input.append(list('5 * 9 * ( 7 * 3 * 3 + 9 * 3 + ( 8 + 6 * 4 ) )'.split(' ')))
        actual = part2(input)
        self.assertEqual(669060, actual)

if __name__ == '__main__':
    unittest.main()
