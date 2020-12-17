from console import sc
from console.constants import ESC
from console.utils import wait_key
import re
import math

def readInput(filename): 
    inputFile = open(filename)
    lines = [list(line) for line in [line.rstrip('\n') for line in inputFile]]
    inputFile.close()

    space = dict()
    y = math.ceil(0 - (len(lines) / 2))
    for line in lines:
        x = math.ceil(0 - (len(line) / 2))
        for char in line:
            space[(x,y,0,0)] = char
            x = x + 1
        y = y + 1
    return space

def isActive(space, x, y, z, w):
    activeAround = 0
    for dw in range(-1, 2):
        for dz in range(-1, 2):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (x+dx, y+dy, z+dz, w+dw) in space:
                        if space[(x+dx, y+dy, z+dz, w+dw)] == '#' and (dx != 0 or dy != 0 or dz != 0 or dw != 0):
                            activeAround = activeAround + 1
    if (x,y,z,w) in space and space[(x,y,z,w)] == '#':
        if 2 <= activeAround <= 3:
            return '#'
        return '.'
    if activeAround == 3:
        return '#'
    return '.'

def boot(space, dims):
    minZ = maxZ = minW = maxW =0
    minX = min(space, key = lambda k: k[0])[0]
    maxX = max(space, key = lambda k: k[0])[0]
    minY = min(space, key = lambda k: k[1])[1]
    maxY = max(space, key = lambda k: k[1])[1]
    for i in range(0, 6):
        newSpace = dict()
        minX = minX - 1
        maxX = maxX + 1
        minY = minY - 1
        maxY = maxY + 1
        minZ = minZ - 1
        maxZ = maxZ + 1
        if dims == 4:
            minW = minW - 1
            maxW = maxW + 1
        for w in range(minW, maxW + 1):
            for z in range(minZ, maxZ + 1):
                for y in range(minY, maxY + 1):
                    for x in range(minX, maxX + 1):
                        newSpace[(x,y,z,w)] = isActive(space, x, y, z,w)
        space = newSpace
    actives = 0
    for key in space:
        if space[key] == '#':
            actives = actives + 1
    return actives

def part1(input):
    result = boot(input, 3)
    return result

def part2(input):
    result = boot(input, 4)
    return result

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            space = readInput('input.txt')
            result = part1(space)
            print('Part 1 actives:', result)
            result = part2(space)
            print('Part 2 actives:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
