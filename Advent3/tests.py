import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.rows = readInput('testinput.txt')
        
    def test_part1(self):
        result = part1(self.rows)
        self.assertEqual(7, result)

    def test_part2(self):
        result = part2(self.rows)
        self.assertEqual(336, result)

if __name__ == '__main__':
    unittest.main()