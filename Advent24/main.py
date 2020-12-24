from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

def readInput(filename):
    inputFile = open(filename)
    regex = re.compile('(e|(se)|(sw)|w|(nw)|(ne))')
    paths = [[x[0] for x in regex.findall((line.rstrip('\n')))] for line in inputFile]
    inputFile.close()
    return paths

class tile():
    def __init__(self, tiles, key):
        self.tiles = tiles
        self.key = key
        self.color = 'white'
    
    def e(self):
        x = self.key[0] + 1
        y = self.key[1]
        newKey = (x,y)
        return self.getOrMakeTile(newKey)

    def se(self):
        if self.key[1] % 2 == 0:
            x = self.key[0]
        else:
            x = self.key[0] + 1
        y = self.key[1] - 1
        newKey = (x,y)
        return self.getOrMakeTile(newKey)

    def sw(self):
        if self.key[1] % 2 == 0:
            x = self.key[0] - 1
        else:
            x = self.key[0]
        y = self.key[1] - 1
        newKey = (x,y)
        return self.getOrMakeTile(newKey)

    def w(self):
        x = self.key[0] - 1
        y = self.key[1]
        newKey = (x,y)
        return self.getOrMakeTile(newKey)

    def nw(self):
        if self.key[1] % 2 == 0:
            x = self.key[0] - 1
        else:
            x = self.key[0]
        y = self.key[1] + 1
        newKey = (x,y)
        return self.getOrMakeTile(newKey)

    def ne(self):
        if self.key[1] % 2 == 0:
            x = self.key[0]
        else:
            x = self.key[0] + 1
        y = self.key[1] + 1
        newKey = (x,y)
        return self.getOrMakeTile(newKey)

    def getOrMakeTile(self, newKey):
        if newKey in self.tiles:
            return self.tiles[newKey]
        else:
            newTile = tile(self.tiles, newKey)
            self.tiles[newKey] = newTile
            return newTile

    def flip(self):
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'

    def folow(self, direction):
        tile = getattr(self, direction)()
        return tile

def prepare(paths):
    tiles = dict()
    center = tile(tiles, (0,0))
    for path in paths:
        current = center
        for step in path:
            current = current.folow(step)
        current.flip()
    result = len([t for t in tiles.values() if t.color=='black'])
    return (result, tiles)

def part1(paths):
    result = prepare(paths)
    return result[0]

def applyRules(tiles):
    toFlip = list()
    for tile in [t for t in tiles.values()]:
        for d in ['e','se','sw','w','nw','ne']:
            tile.folow(d)
    for tile in [t for t in tiles.values()]:
        surroundBlack = len([t for t in [tile.folow(d) for d in ['e','se','sw','w','nw','ne']] if t.color=='black'])
        if tile.color == 'black':
            if not 0 < surroundBlack <= 2:
                toFlip.append(tile)
        else:
            if surroundBlack == 2:
                toFlip.append(tile)
    for tile in toFlip:
        tile.flip()

def part2(paths):
    x, tiles = prepare(paths)
    for i in range(100):
        applyRules(tiles)
    result = len([t for t in tiles.values() if t.color=='black'])    
    return result

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            input = readInput('input.txt')
            result = part1(input)
            print('Part 1 black:', result)
            input = readInput('input.txt')
            result = part2(input)
            print('Part 2 black:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
