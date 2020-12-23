import unittest
from main import part1, part2

class TestParts(unittest.TestCase):
    def test_part1(self):
        actual = part1('389125467')
        self.assertEqual('67384529', actual)

    def test_part2(self):
        actual = part2('389125467')
        self.assertEqual(149245887792, actual)

if __name__ == '__main__':
    unittest.main()
