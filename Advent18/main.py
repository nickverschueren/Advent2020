from console import sc
from console.constants import ESC
from console.utils import wait_key
import re
import math

def readInput(filename): 
    inputFile = open(filename)
    lines = [list(line.replace('(','( ').replace(')',' )').split(' ')) for line in [line.rstrip('\n') for line in inputFile]]
    inputFile.close()
    return lines

def evaluate(input, position):
    register = 0
    operation = ''
    while position < len(input):
        value = 0
        current = input[position]
        if current == ')':
            return (register, position)
        elif current == '(':
            value, position = evaluate(input, position + 1)
        elif current.isnumeric():
            value = int(current)
        else:
            operation = current
            position = position + 1
            continue
        if operation == '':
            register = value
        elif operation == '+':
            register = register + value
        elif operation == '*':
            register = register * value
        position = position + 1
    return (register, position)

def addBraces(input):
    p = 0
    while p < len(input):
        if input[p] == '+':
            braces = 0
            q = p
            while q < len(input):
                if braces == 0 and input[q] == '*':
                    break
                elif input[q] == '(':
                    braces = braces + 1
                elif input[q] == ")":
                    braces = braces - 1
                if braces < 0:
                    break
                q = q + 1
            input.insert(q, ')')
            q = p
            braces = 0
            while q >= 0:
                if braces == 0 and input[q] == '*':
                    break
                elif input[q] == '(':
                    braces = braces - 1
                elif input[q] == ")":
                    braces = braces + 1
                if braces < 0:
                    break
                q = q - 1
            input.insert(q + 1, '(')
            p = p + 1
        p = p + 1

def evaluate2(input):
    addBraces(input)    
    return evaluate(input, 0)[0]

def part1(input):
    return sum([evaluate(line, 0)[0] for line in input])

def part2(input):
    results = [evaluate2(line) for line in input]
    return sum(results)

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            lines = readInput('input.txt')
            result = part1(lines)
            print('Part 1 sum:', result)
            result = part2(lines)
            print('Part 2 sum:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
