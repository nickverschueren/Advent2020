import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.groups = readInput('testinput.txt')
        
    def test_part1(self):
        actual = part1(self.groups)
        self.assertEqual(11, actual)

    def test_part2(self):
        actual = part2(self.groups)
        self.assertEqual(6, actual)

if __name__ == '__main__':
    unittest.main()