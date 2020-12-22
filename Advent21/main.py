from console import sc
from console.constants import ESC
from console.utils import wait_key

def readInput(filename):
    with open(filename) as file:
        data = file.read()
    labels = data.split('\n')
    parsed = [[p.replace(',','').split(' ') for p in label.replace(')','').split(' (contains ')] for label in labels if label != '']
    return parsed

def countIngredients(foods):
    counts = dict()
    for food in foods:
        for i in food[0]:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
    return counts

def getAllergens(foods):
    algs = dict()
    for food in foods:
        for a in food[1]:
            if a in algs:
                algs[a] = set(algs[a] & set(food[0]))
            else:
                algs[a] = set(food[0])
    return algs

def part1(foods):
    ingredients = countIngredients(foods)
    algs = getAllergens(foods)
    clear = dict(ingredients)
    for i in ingredients:
        for a in algs:
            if i in algs[a] and i in clear:
                clear.pop(i)
    return sum([i for i in clear.values()])

def cleanup(algs):
    algList = [(a, algs[a]) for a in algs]

    while len(algList) > 0:
        algList.sort(key=lambda a: len(a[1]))
        a  = algList[0]
        algs[a[0]] = a[1]
        algList.remove(a)
        x = next(iter(a[1]))
        for r in algList:
            if x in r[1]:
                r[1].remove(x)
    return algs

def part2(foods):
    algs = getAllergens(foods)
    algs = cleanup(algs)
    algList = [(a, algs[a]) for a in algs]
    algList.sort(key=lambda a: a[0])
    result = ",".join([",".join(a[1]) for a in algList])
    return result

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            foods = readInput('input.txt')
            result = part1(foods)
            print('Part 1 score:', result)
            result = part2(foods)
            print('Part 2 valid:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
