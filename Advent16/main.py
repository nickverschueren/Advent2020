from console import sc
from console.constants import ESC
from console.utils import wait_key
import re

def readInput(filename): 
    inputFile = open(filename)
    lines = [line for line in [line.rstrip('\n') for line in inputFile]]
    inputFile.close()

    index = 0
    rules = dict()
    while len(lines[index])>0:
        parts = lines[index].split(': ')
        rules[parts[0]] = list([(int(s[0]),int(s[1])) for s in [g.split('-') for g in parts[1].split(' or ')]])
        index = index + 1
    
    index = index + 2
    myTicket = list([int(n) for n in lines[index].split(',')])

    index = index + 3
    nearbyTickets = list()
    for line in lines[index:]:
        nearbyTickets.append(list([int(n) for n in line.split(',')]))

    return (rules, myTicket, nearbyTickets)

def isValid(rules, number):
    for rule in rules:
        for range in rules[rule]:
            if range[0] <= number <= range[1]:
                return True
    return False

def filterTickets(rules, tickets):
    valids = list()
    for ticket in tickets:
        ok = True
        for number in ticket:
            if not isValid(rules, number):
                ok = False
                break
        if ok:
            valids.append(ticket)
    return valids

def isNumberValidForRule(rule, number):
    for range in rule:
        if range[0] <= number <= range[1]:
            return True
    return False

def discoverFields(rules, tickets):
    found = dict()
    for rule in rules:
        found[rule] = set(range(len(tickets[0])))
    for ticket in tickets:
        for i, number in enumerate(ticket):
            for rule in found:
                if not isNumberValidForRule(rules[rule], number) and i in found[rule]:
                    found[rule].remove(i)
    cleaned = [(rule, found[rule]) for rule in found]
    cleaned.sort(key = lambda x: len(x[1]))
    for i in range(len(cleaned)):
        for j in range(i + 1, len(cleaned)):
            for x in cleaned[i][1]:
                cleaned[j][1].remove(x)
    return [(field[0], field[1].pop()) for field in cleaned]

def getProduct(fields, ticket):
    product = 1
    for field in fields:
        if field[0].startswith('departure'):
            product = product * ticket[field[1]]
    return product

def part1(input):
    sum = 0
    for ticket in input[2]:
        for number in ticket:
            if not isValid(input[0], number):
                sum = sum + number
    return sum

def part2(input):
    valids = filterTickets(input[0], input[2])
    fields = discoverFields(input[0], valids)
    product = getProduct(fields, input[1])
    return product

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            input = readInput('input.txt')
            result = part1(input)
            print('Part 1 error rate:', result)
            result = part2(input)
            print('Part 2 product:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
