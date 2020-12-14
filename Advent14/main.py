from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

def readInput(filename): 
    inputFile = open(filename)
    instructions = [(instruction[0], instruction[1]) for instruction in [line.rstrip('\n').split(' = ') for line in inputFile] if len(instruction) > 1]
    inputFile.close()
    return instructions

def part1(program):
    memory = dict()
    maskAnd = 0x0
    maskOr = 0x0
    for instruction in program:
        if instruction[0] == 'mask':
            maskAnd = int(instruction[1].replace('X','1'), 2)
            maskOr = int(instruction[1].replace('X','0'), 2)
        else:
            pos = int(instruction[0][4:len(instruction[0])-1])
            memory[pos] = (int(instruction[1]) & maskAnd) | maskOr
    result = sum(memory.values())
    return result

def part2(program):
    memory = dict()
    mask = ""
    xes = 0
    combos = 0
    for instruction in program:
        if instruction[0] == 'mask':
            mask = instruction[1]
            xes = [m.start() for m in re.finditer('X', mask)]
            combos = 2 ** mask.count('X')
        else:
            pos = int(instruction[0][4:len(instruction[0])-1])
            for i in range(0, combos):
                maskAnd = list(mask.replace('0','1').replace('X','1'))
                maskOr = list(mask.replace('X','0'))
                k = 0
                for j in xes:
                    if i & (1 << k):
                        maskOr[j] = '1'
                    else:
                        maskAnd[j] = '0'
                    k = k + 1
                newPos = (pos & int("".join(maskAnd),2)) | int("".join(maskOr),2)
                memory[newPos] = int(instruction[1])
    result = sum(memory.values())
    return result

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            program = readInput('input.txt')
            result = part1(program)
            print('Part 1 sum:', result)
            result = part2(program)
            print('Part 2 sum:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
