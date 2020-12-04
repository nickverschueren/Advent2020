from console import sc
from console.constants import ESC
from console.utils import wait_key
from rules import rulesPart1, rulesPart2 

def readInput(filename): 
    records = []
    inputFile = open(filename)
    recordsRaw = [rec.split(' ') for rec in inputFile.read().replace('\n',' ').split('  ')]
    inputFile.close()

    for rec in recordsRaw:
        record = {}
        for field in rec:
            if field == '':
                continue
            parts = field.split(':')
            record[parts[0]] = parts[1]
        records.append(record)
    return records

def part1(records):
    return rulesPart1().validateRecords(records)

def part2(records):
    return rulesPart2().validateRecords(records)

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            records = readInput('input.txt')
            result = part1(records)
            print('Part 1 count:', result)
            result = part2(records)
            print('Part 2 count:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)