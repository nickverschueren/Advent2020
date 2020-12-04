import unittest
from main import readInput, part1, part2

class TestParts(unittest.TestCase):        
    def test_part1(self):
        records = readInput('testinput.txt')
        result = part1(records)
        self.assertEqual(2, result)

    def test_part2_invalid(self):
        records = readInput('testinput2.txt')
        result = part2(records)
        self.assertEqual(0, result)

    def test_part2_valid(self):
        records = readInput('testinput3.txt')
        result = part2(records)
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()