from console import sc
from console.constants import ESC
from console.utils import wait_key

def readInput(filename): 
    inputFile = open(filename)
    groups = [group.rstrip('\n') for group in inputFile.read().split('\n\n')]
    inputFile.close()
    return groups

def countUnique(string):
    letters = set([char for char in string if char != '\n'])
    return len(letters)

def countAll(string):
    letters = {}
    count = 1
    for char in string:
        if char == '\n':
            count += 1
            continue
        if char in letters:
            letters[char] = letters[char] + 1
        else:
            letters[char] = 1
    result = 0
    for letter in letters.keys():
        if letters[letter] == count:
            result = result + 1
    return result

def part1(groups):
    sum = 0
    for group in groups:
        sum = sum + countUnique(group)
    return sum

def part2(groups):
    sum = 0
    for group in groups:
        sum = sum + countAll(group)
    return sum

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            groups = readInput('input.txt')
            result = part1(groups)
            print('Part 1 sum:', result)
            result = part2(groups)
            print('Part 2 sum:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)