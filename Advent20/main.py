from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

class tile():
    def __init__(self, number, lines):
        self.number = number
        self.lines = lines
        self.getHashes()

    def rotate(self):
        l = len(self.lines)
        lines = [''.join([self.lines[x][y] for x in range(l)]) for y in range(l-1,-1,-1)]
        self.lines = lines
        self.getHashes()

    def flip(self):
        l = len(self.lines)
        lines = [l for l in self.lines[::-1]]
        self.lines = lines
        self.getHashes()

    def getHashes(self):
        hashes = list()
        altHashes = list()
        for side in range(4):
            hash = ""
            if side % 2 == 0:
                if side == 0:
                    hash = self.lines[0]
                else:
                    hash = self.lines[len(self.lines) - 1]       
            else:
                if side == 1:
                    hash = "".join([l[len(l) - 1] for l in self.lines])
                else:
                    hash = "".join([l[0] for l in self.lines])
            hashes.append(int(hash.replace('.', '0').replace('#', '1'), 2))
            altHashes.append(int(hash.replace('.', '0').replace('#', '1')[::-1], 2))
        self.hashes = hashes
        self.altHashes = altHashes

    def orientTile(self, hash, side):
        i = 0
        while self.hashes[side] != hash:
            if i % 4 == 3:
                self.flip()
            else:
                self.rotate()
            i += 1

    def print(self):
        for l in self.lines:
            print(l)

def processImage(img):
    lines = img.split('\n')
    number = int(lines[0].replace('Tile ','').replace(':',''))
    return tile(number, lines[1:])

def readInput(filename):
    with open(filename) as file:
        data = file.read()
    images = data.split('\n\n')
    images = dict({p.number: p for p in [processImage(img) for img in images if len(img) > 1]})
    return images

def iscorner(hashes, img, tile):
    matches = 0
    for hi in tile.hashes + tile.altHashes:
        for h in hashes:
            if h[0] == hi and h[1] != img:
                matches += 1
                if matches >= 5:
                    return False
    return True

def part1(input):
    allHashes = list()
    for img in input:
        for hash in input[img].hashes:
            allHashes.append((hash, img))
        for hash in input[img].altHashes:
            allHashes.append((hash, img))        
    corners = [img for img in input if iscorner(allHashes, img, input[img])]
    result = 1
    for c in corners:
        result *= c
    return result

def flipRow(input, tiles):
    for x in tiles[0]:
        tile = input[x]
        tile.flip()

def findhash(hashes, hash, nr):
    f = [h for h in hashes if h[0] == hash and h[1] != nr]
    return len(f) > 0

def orientfirst(tile, nr, hashes):
    while True:
        if (findhash(hashes, tile.hashes[1], nr) and findhash(hashes, tile.hashes[2], nr)):
            return tile
        tile.rotate()

def findTiles(input, topleft, hashes):
    tiles = list()
    sizex = sizey = int(len(input) ** .5)
    for y in range(sizey):
        nexth = 0
        tile = ""
        for x in range(sizex):
            if(x == 0 and y == 0):
                tile = input[topleft]
                tile = orientfirst(tile, topleft, hashes)
                input[topleft] = tile
                nexth = tile.hashes[1]
                tiles.append(list([topleft]))
            elif(x == 0):
                nexth = input[tiles[y-1][0]].hashes[2]
                next = [h[1] for h in hashes if h[1] != tiles[y-1][0] and h[0] == nexth]
                if not next and y == 1:
                    flipRow(input, tiles)
                    nexth = input[tiles[y-1][0]].hashes[2]
                    next = [h[1] for h in hashes if h[1] != tiles[y-1][0] and h[0] == nexth]
                tiles.append(list([next[0]]))
                tile = input[next[0]]
                tile.orientTile(nexth, 0)
                nexth = tile.hashes[1]
            else:
                next = [h[1] for h in hashes if h[1] != tiles[y][x-1] and h[0] == nexth][0]
                tiles[y].append(next)
                tile = input[next]
                tile.orientTile(nexth, 3)
                nexth = tile.hashes[1]
    return tiles

def stichTiles(input, tiles):
    image = list()
    tileSize = len(input[tiles[0][0]].lines)
    for y in range(len(tiles)):
        for ty in range(1,tileSize-1):
            image.append(''.join([input[l].lines[ty][1:tileSize-1] for l in [i for i in tiles[y]]]))
    return image

def countNonBlanks(image):
    count = 0
    for line in image.lines:
        count += str.count(line,'#')
    return count

def maches(input, pattern):
    for x in range(len(pattern)):
        if pattern[x] == '#' and input[x]=='.':
            return False
    return True

def findmonsters(image):
    count = 0
    pattern0 = '                  # '
    pattern1 = '#    ##    ##    ###'
    pattern2 = ' #  #  #  #  #  #   '    
    for x in range(len(image.lines[0])-20):
        for y in range(1,len(image.lines)-1):
            if maches(image.lines[y][x:x+20], pattern1) and maches(image.lines[y-1][x:x+20], pattern0) and maches(image.lines[y+1][x:x+20], pattern2):
                count += 1
                image.lines[y-1] = replacePattern(image.lines[y-1], pattern0, x)
                image.lines[y] = replacePattern(image.lines[y], pattern1, x)
                image.lines[y+1] = replacePattern(image.lines[y+1], pattern2, x)
    return count

def replacePattern(input, pattern, position):
    output = input
    for x in range(len(pattern)):
        if(pattern[x] == '#'):
            output = output[0:position+x] + "O" + output[position+x+1: len(output)]
    return output

def countmonsters(image):
    count = 0
    i = 0
    while True:
        count = findmonsters(image)
        if count > 0:
            break
        if i % 4 == 3:
            image.flip()
        else:
            image.rotate()
        i += 1
    return count

def buildimage(input, topleft, hashes):
    tiles = findTiles(input, topleft, hashes)
    image = stichTiles(input, tiles)
    return tile(0, image)

def part2(input):
    allHashes = list()
    for img in input:
        for hash in input[img].hashes:
            allHashes.append((hash, img))
        for hash in input[img].altHashes:
            allHashes.append((hash, img))
    corners = [img for img in input if iscorner(allHashes, img, input[img])]
    image = buildimage(input, corners[0], allHashes)
    monsters = countmonsters(image)
    total = countNonBlanks(image)

    return total

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            input = readInput('input.txt')
            result = part1(input)
            print('Part 1 corners:', result)
            result = part2(input)
            print('Part 2 non-blank:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
