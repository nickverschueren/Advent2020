from console import sc
from console.constants import ESC
from console.utils import wait_key

def readInput(): 
    inputFile = open('input.txt')
    rows = [line.rstrip('\n') for line in inputFile]
    inputFile.close()
    return rows

def countTrees(rows, dx, dy):
    x = 0
    trees = 0
    for y in range(0, len(rows), dy):
        row = rows[y]
        if row[x] == '#':
            trees = trees + 1
        x = (x + dx) % len(row)
    return trees

def part1(rows):
    return countTrees(rows, 3, 1)

def part2(rows):
    result = countTrees(rows, 1, 1)
    result = result * countTrees(rows, 3, 1)
    result = result * countTrees(rows, 5, 1)
    result = result * countTrees(rows, 7, 1)
    result = result * countTrees(rows, 1, 2)
    return result

with sc.fullscreen():
    with sc.location(0, 4):
        rows = readInput()
        result = part1(rows)
        print('Part 1 trees:', result)
        result = part2(rows)
        print('Part 2 product:', result)
    
    with sc.location(5, 8):
        with sc.hidden_cursor():
            print('Press ESC to exit')
            wait_key(ESC)