from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

def readInput(filename): 
    inputFile = open(filename)
    numbers = [numbers for numbers in [line.rstrip('\n').split(',') for line in inputFile]]
    inputFile.close()
    return [int(i) for i in numbers[0]]

def count(seed, end):
    memory = dict()
    for i, n in enumerate(seed):
        memory[n] = list([i + 1])
    prev = seed[len(seed) - 1]
    for i in range(len(seed), end):
        next = 0
        if len(memory[prev]) > 1:
            next = memory[prev][len(memory[prev])-1] - memory[prev][len(memory[prev])-2]
        if next not in memory:
            memory[next] = list([i + 1])
        else:
            memory[next].append(i + 1)
        prev = next

    return prev

def part1(seed):
    return count(seed, 2020)

def part2(seed):
    return count(seed, 30000000)

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            numbers = readInput('input.txt')
            result = part1(numbers)
            print('Part 1 2020th:', result)
            result = part2(numbers)
            print('Part 2 30000000th:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
