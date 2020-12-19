from console import sc
from console.constants import ESC
from console.utils import wait_key
from math1Calculator import math1Calculator
from math2Calculator import math2Calculator

def part1(filename):
    return math1Calculator().processFile(filename)

def part2(filename):
    return math2Calculator().processFile(filename)

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            result = part1('input.txt')
            print('Part 1 sum:', result)
            result = part2('input.txt')
            print('Part 2 sum:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
