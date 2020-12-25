from console import sc
from console.constants import ESC
from console.utils import wait_key
import math

def transform(i, s):
    return (s * i) % 20201227

def findExp(number):
    e = 0
    i = 1
    while i != number:
        i = transform(i, 7)
        e += 1
    return e

def part1(card, door):
    doorLoop = findExp(door)
    key = 1
    for i in range(doorLoop):
        key = transform(key, card)
    return key

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            result = part1(15113849, 4206373)
            print('Part 1 key:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
