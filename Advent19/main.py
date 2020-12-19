from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

def readInput(filename):
    with open(filename) as file:
        data = file.read()
    parts = data.split('\n\n')
    rules = [(rule[0],rule[1]) for rule in [line.split(': ') for line in parts[0].split('\n')]]
    messages = [line for line in parts[1].split('\n')]
    return (rules, messages)

def buildRe(rules):
    temp = dict()
    for key, rule in [(x[0], x[1]) for x in rules]:
        if rule.startswith('"'):
            temp[key] = f' { rule[1:2] } '
        elif rule.find('|') >= 0:
            temp[key] = f' ( ( { str.replace(rule,"|",") | (") } ) ) '
        else:
            temp[key] = f' { rule } '
    keys = list([i for i in temp if i != '0'])
    keys.sort()
    for i in keys:
        a = temp.pop(i)
        for j in temp:
            b = f' {i} '
            r = str.replace(temp[j], b, a)
            r = str.replace(r, b, a)
            temp[j] = r
    expr = f'^{str.replace(temp["0"]," ","")}$'
    return expr

def part1(input):
    expr = buildRe(input[0])
    matcher = re.compile(expr)
    matched = [msg for msg in input[1] if matcher.match(msg)]
    return len(matched)

def formatRules(rules):
    return dict({ int(rule[0]) : [[y for y in x.split(' ') if y != ''] for x in rule[1].split('|')] for rule in rules })

def getMatches(rules, input, position, rule_id):
    matches = list()
    if position >= len(input):
        return matches
    rule = rules[rule_id]
    for case in rule:
        if case[0].startswith('"'):
            if input[position] == case[0][1]:
                matches.append(position + 1)
            else:
                continue
        else:
            cm = list([position])
            for child in case:
                newcm = list()
                for i in cm:
                    newcm = newcm + getMatches(rules, input, i, int(child))
                cm = newcm
            matches = matches + cm
    return matches

def anyCompleteMatches(rules, input):
    matches = [m for m in getMatches(rules, input, 0, 0) if m == len(input)]
    return len(matches) > 0

def part1b(input):
    rules = formatRules(input[0])
    matches = [msg for msg in input[1] if anyCompleteMatches(rules, msg)]
    return len(matches)

def changeRules(rules):
    rules[8] = [['42'],['42','8']]
    rules[11] = [['42','31'],['42','11','31']]

def part2(input):
    rules = formatRules(input[0])
    changeRules(rules)
    matches = [msg for msg in input[1] if anyCompleteMatches(rules, msg)]
    return len(matches)

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            input = readInput('input.txt')
            result = part1(input)
            print('Part 1 valid:', result)
            result = part1b(input)
            print('Part 1b valid:', result)
            result = part2(input)
            print('Part 2 valid:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
