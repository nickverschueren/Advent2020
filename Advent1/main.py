from console import sc
from console.constants import ESC
from console.utils import wait_key

def readInput(): 
    inputFile = open('input.txt')
    values = [int(line) for line in inputFile]
    inputFile.close()
    return values

def part1(values):
    for value1 in values:
        for value2 in values:
            if(value1 + value2 == 2020):
                print(value1, value2, value1 * value2)
                return

def part2(values):
    for value1 in values:
        for value2 in values:
            if (value1 + value2 >= 2020):
                break

            for value3 in values:
                if(value1 + value2 + value3 == 2020):
                    print(value1, value2, value3, value1 * value2 * value3)
                    return

with sc.fullscreen():
    with sc.location(0, 4):
        values = readInput()
        part1(values)
        part2(values)
    
    with sc.location(5, 8):
        with sc.hidden_cursor():
            print('Press ESC to exit')
            wait_key(ESC)