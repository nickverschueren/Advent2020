from console import sc
from console.constants import ESC
from console.utils import wait_key
from processor import processor as prc
from processor import processor2 as prc2
import math
import re

def readInput(filename): 
    inputFile = open(filename)
    instructions = [(instruction[0], int(instruction[1:])) for instruction in [line.rstrip('\n') for line in inputFile] if len(instruction) > 1]
    inputFile.close()

    return instructions

def part1(program):
    eof = len(program)
    processor = prc(program)
    ended = False
    while not processor.finished():
        processor.executeCurrent()
    return (processor.accumulator_x, processor.accumulator_y, abs(processor.accumulator_x) + abs(processor.accumulator_y))

def part2(program):
    eof = len(program)
    processor = prc2(program)
    ended = False
    while not processor.finished():
        processor.executeCurrent()        
    return (processor.accumulator_x, processor.accumulator_y, abs(processor.accumulator_x) + abs(processor.accumulator_y))

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            program = readInput('input.txt')
            result = part1(program)
            print('Part 1 position:', result)
            result = part2(program)
            print('Part 2 position:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
