from console import sc
from console.constants import ESC
from console.utils import wait_key

class cup():
    def __init__(self, label):
        self.label = label
    def setNext(self,next):
        self.next = next
    def cut3(self):
        a = self.next
        b = a.next
        c = b.next
        self.next = c.next
        c.setNext(None)
        return [a,b,c]
    def paste3(self, toInsert):
        d = self.next
        self.setNext(toInsert[0])
        toInsert[2].setNext(d)

def playRound(cups, current):
    toMove = current.cut3()
    labelsToMove = [x.label for x in toMove]
    count = len(cups)
    j = current.label - 1
    if j < 1:
        j += count
    while j in labelsToMove:
        j -= 1
        if j < 1:
            j += count
    dest = cups[j]
    dest.paste3(toMove)
    return current.next

def out(cups):
    i = cups[1].next
    result = list()
    while not i.label == 1:
        result.append(i.label)
        i = i.next
    return ''.join([str(i) for i in result])

def play(labels, iterations):
    cups = dict()
    prev = None
    for i in labels:
        c = cup(i)
        if prev:
            prev.setNext(c)
        cups[i] = c
        prev = c
    current = cups[labels[0]]
    prev.setNext(current)
    pointer = 0
    for i in range(iterations):
        current = playRound(cups, current)
    return cups

def part1(input):
    labels = [int(c) for c in input]
    cups = play(labels, 100)
    return out(cups)

def part2(input):
    labels = [int(c) for c in input]
    for i in range(len(input) + 1, 1000001):
        labels.append(i)
    cups = play(labels, 10000000)
    i = cups[1].next
    return i.label * i.next.label

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            result = part1('789465123')          
            print('Part 1 positions:', result)
            result = part2('789465123')
            print('Part 2 product:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
