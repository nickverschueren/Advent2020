from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

def readInput(filename):
    inputFile = open(filename)
    ratings = [int(line.rstrip('\n')) for line in inputFile]
    ratings.insert(0, 0)
    ratings.sort()
    inputFile.close()

    return ratings

def part1(ratings):
    prev = 0
    difs = dict([(1,0),(2,0),(3,1)])
    for r in ratings[1:]:
        difs[r-prev] = difs[r-prev] + 1
        prev = r
    return difs[1] * difs[3]

def part2(ratings):
    sums = { ratings[len(ratings)-1] : 1 }
    for x in range(len(ratings)-2, -1, -1):
        sum = 0
        for y in range(1,4):
            if x < len(ratings) and ratings[x] + y in sums:
                sum = sum + sums[ratings[x] + y]
        sums[ratings[x]] = sum
    return sums[0]

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            ratings = readInput('input.txt')
            result = part1(ratings)
            print('Part 1 dif1 * dif3:', result)
            result = part2(ratings)
            print('Part 2 combos:', result)

        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
