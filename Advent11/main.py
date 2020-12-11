from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

def readInput(filename):
    inputFile = open(filename)
    rows = [list(line.rstrip('\n')) for line in inputFile]
    inputFile.close()
    return rows

def isOccupied(rows, x, y):
    if 0 <= x < len(rows[0]):
        if 0 <= y < len(rows):
            return rows[y][x] == '#'
    return False

def countOccupied(rows, x1, y1, x2, y2):
    sum = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if isOccupied(rows,x,y):
                sum = sum + 1
    return sum

def applyRules(rows):
    newRows = [[cell for cell in row] for row in rows]
    changes = 0
    for x in range(0, len(rows[0])):
        for y in range(0, len(rows)):
            if rows[y][x] == '.':
                continue
            count = countOccupied(rows, x-1, y-1, x + 1, y + 1)
            if count == 0:
                newRows[y][x] = '#'
                changes = changes + 1
            elif rows[y][x] == '#' and count > 4:
                newRows[y][x] = 'L'
                changes = changes + 1
    return (newRows, changes)            

def find(rows, x, y, dx, dy):
    x = x + dx
    y = y + dy
    while 0 <= x < len(rows[0]) and 0 <= y < len(rows):
        if rows[y][x]=='L':
            return 0
        elif rows[y][x] == '#':
            return 1
        x = x + dx
        y = y + dy
    return 0

def countOccupied2(rows, x, y):
    sum = find(rows, x, y, 1, 0) + find(rows, x, y, 1, 1) + find(rows, x, y, 0, 1)
    sum = sum + find(rows, x, y, -1, 1) + find(rows, x, y, -1, 0) + find(rows, x, y, -1, -1)
    sum = sum + find(rows, x, y, 0, -1) + find(rows, x, y, 1, -1)
    return sum

def applyRules2(rows):
    newRows = [[cell for cell in row] for row in rows]
    changes = 0
    for x in range(0, len(rows[0])):
        for y in range(0, len(rows)):
            if rows[y][x] == '.':
                continue
            count = countOccupied2(rows, x, y)
            if rows[y][x] == 'L' and count == 0:
                newRows[y][x] = '#'
                changes = changes + 1
            elif rows[y][x] == '#' and count >= 5:
                newRows[y][x] = 'L'
                changes = changes + 1
    return (newRows, changes)            

def part1(rows):
    changes = 1
    while changes > 0:
        rows, changes = applyRules(rows)
    return countOccupied(rows,0,0,len(rows[0]), len(rows))

def part2(rows):
    changes = 1
    while changes > 0:
        rows, changes = applyRules2(rows)
    return countOccupied(rows,0,0,len(rows[0]), len(rows))

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            rows = readInput('input.txt')
            result = part1(rows)
            print('Part 1 occupied:', result)
            result = part2(rows)
            print('Part 2 occupied:', result)

        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
