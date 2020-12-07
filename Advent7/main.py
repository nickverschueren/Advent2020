from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

def readInput(filename): 
    inputFile = open(filename)
    lines = [line.rstrip('\n') for line in inputFile]
    inputFile.close()

    rules = {}
    for line in lines:
        matches = re.findall(r"(?P<count>(\d+|no)\s)?(?P<color>(\w+\s){1,2})bag", line)
        container = matches[0][2].rstrip(' ')
        rules[container] = dict([(m[2].rstrip(' '),int(m[0].replace('no','0'))) for m in matches[1:]])

    return rules

def part1(rules):
    added = 1
    find = ['shiny gold']
    colors = set()
    while added > 0:
        newfind=[]
        for f in find:
            for r in rules:
                if f in rules[r]:
                    newfind.append(r) 
        before = len(colors)
        colors.update(newfind)
        added = len(colors) - before
        find = newfind
    return len(colors)

def recurse(rules, name):
    sum = 0
    if not name in rules:
        return 0
    rule = rules[name]
    for r in rule:
        sum = sum + (rule[r] * (1 + recurse(rules, r)))
    return sum

def part2(rules):
    return recurse(rules, 'shiny gold')

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            rules = readInput('input.txt')
            result = part1(rules)
            print('Part 1 gold in:', result)
            result = part2(rules)
            print('Part 2 in gold:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)