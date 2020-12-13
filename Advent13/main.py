from console import sc
from console.constants import ESC
from console.utils import wait_key
from chinese import *
import math

def readInput(filename): 
    inputFile = open(filename)
    lines = [line.rstrip('\n') for line in inputFile]
    time = int(lines[0])
    busses = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    inputFile.close()
    return (time, busses)

def readInput2(filename): 
    inputFile = open(filename)
    lines = [line.rstrip('\n') for line in inputFile]
    busses = [(offset, int(bus)) for offset, bus in enumerate([bus for bus in lines[1].split(',')]) if bus !='x']
    inputFile.close()
    return busses

def part1(input):
    closest = [(bus, bus * (math.ceil(input[0] / bus))) for bus in input[1]] 
    closest.sort(key = lambda c : c[1])
    result = closest[0]
    return ((result[1] - input[0]) * result[0])

def part2(input):
    remainders = [(x[1] - x[0]) % x[1] for x in input]
    moduli = [x[1] for x in input]
    result = findMinX(moduli, remainders, len(moduli))
    return result

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            input = readInput('input.txt')
            result = part1(input)
            print('Part 1 result:', result)
            offsets = readInput2('input.txt')
            result = part2(offsets)
            print('Part 2 result:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
