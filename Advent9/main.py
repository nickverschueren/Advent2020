from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

def readInput(filename): 
    inputFile = open(filename)
    instructions = [int(line.rstrip('\n')) for line in inputFile]
    inputFile.close()

    return instructions

def isValid(numbers, position, preamble):
    for x in range(position - preamble - 1, position):        
        for y in range(position - preamble, x):
            if numbers[x] + numbers[y] == numbers[position]:
                return True
    return False

def part1(numbers, preamble):
    for x in range(preamble, len(numbers)):
        if not isValid(numbers, x, preamble):
            return (x, numbers[x])
    return (0, 0)

def part2(numbers, find):
    for x in range(len(numbers)):
        sum = numbers[x]
        for y in range(x + 1, len(numbers)):
            sum = sum + numbers[y]
            if sum == find:
                return min(numbers[x:y + 1]) + max(numbers[x:y + 1])
            elif sum > find:
                break
    return 0

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            numbers = readInput('input.txt')
            result = part1(numbers, 25)
            print('Part 1 first invalid:', result)
            result = part2(numbers, result[1])
            print('Part 2 min+max:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
