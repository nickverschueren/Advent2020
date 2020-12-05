from console import sc
from console.constants import ESC
from console.utils import wait_key

def readInput(filename): 
    inputFile = open(filename)
    rows = [line.rstrip('\n') for line in inputFile]
    inputFile.close()
    return rows

def binaryCountStr(string, onSymb = '1'):
    value = 0
    for i in range(len(string)):
        if string[len(string) - i - 1] in onSymb:
            value = value + (2 ** i)
    return value

def part1(tickets):
    seats = [binaryCountStr(ticket,'BR') for ticket in tickets]
    return max(seats)

def part2(tickets):
    seats = [binaryCountStr(ticket,'BR') for ticket in tickets]
    seats.sort()
    for i in range(len(seats)-1):
        if(seats[i] == seats[i + 1] - 2):
            return seats[i] + 1

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            rows = readInput('input.txt')
            result = part1(rows)
            print('Part 1 highest:', result)
            result = part2(rows)
            print('Part 2 my seat:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)