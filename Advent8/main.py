from console import sc
from console.constants import ESC
from console.utils import wait_key
from processor import processor as prc
import re

def readInput(filename): 
    inputFile = open(filename)
    instructions = [(instruction[0], int(instruction[1].replace('+',''))) for instruction in [line.rstrip('\n').split(' ') for line in inputFile] if len(instruction) > 1]
    inputFile.close()

    return instructions

def part1(program):
    executed = set()
    processor = prc(program)
    while not processor.pointer in executed:
        executed.add(processor.pointer)
        processor.executeCurrent()
    return processor.accumulator

def tryRun(program):
    eof = len(program)
    executed = set()
    processor = prc(program)
    ended = False
    while not ended:
        executed.add(processor.pointer)
        processor.executeCurrent()
        ended = processor.pointer in executed or not processor.ready()
    if processor.finished():
        return (True, processor.accumulator)
    return (False, 0)

def part2(program):
    for change in range(len(program)):
        edited = [(t[0], t[1]) for t in program]
        if edited[change][0] == 'jmp':
            edited[change] = ('nop', edited[change][1])
        elif edited[change][0] == 'nop':
            edited[change] = ('jmp', edited[change][1])
        else:
            continue
        
        success, accumulator = tryRun(edited)
        if success:
            return accumulator
    return -1

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            program = readInput('input.txt')
            result = part1(program)
            print('Part 1 accumulator:', result)
            result = part2(program)
            print('Part 2 bug line:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
