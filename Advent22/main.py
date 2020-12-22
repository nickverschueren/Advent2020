from console import sc
from console.constants import ESC
from console.utils import wait_key

def readInput(filename):
    with open(filename) as file:
        data = file.read()
    hands = data.split('\n\n')
    playerHands = [[int(line) for line in hand.split('\n')[1:] if line != ''] for hand in hands]
    return playerHands

def playRound(playerHands):
    p1 = playerHands[0][0]
    p2 = playerHands[1][0]
    playerHands[0].remove(p1)
    playerHands[1].remove(p2)
    if p1 > p2 :
        playerHands[0].append(p1)
        playerHands[0].append(p2)
    else:
        playerHands[1].append(p2)
        playerHands[1].append(p1)

def calculateScore(playerHands):
    return [sum([s*(i+1) for i, s in enumerate(p[::-1])]) for p in playerHands]

def part1(playerHands):
    while len(playerHands[0]) > 0 and len(playerHands[1]) > 0:
        playRound(playerHands)
    return max(calculateScore(playerHands))

def play2(playerHands):
    ended = False
    handmemory = set()
    while not ended:
        m = [':'.join([str(i), ','.join([str(c) for c in hand])]) for i, hand in enumerate(playerHands)]
        for n in m:
            if n in handmemory:
                return 0
            handmemory.add(n)

        p1 = playerHands[0][0]
        p2 = playerHands[1][0]
        playerHands[0].remove(p1)
        playerHands[1].remove(p2)
        winner = 0
        if p1 <= len(playerHands[0]) and p2 <= len(playerHands[1]):
            winner=play2([playerHands[0][0:p1],playerHands[1][0:p2]])
        elif p1 > p2:
            winner = 0
        else:
            winner = 1
        if winner == 0:
            playerHands[0].append(p1)
            playerHands[0].append(p2)
        else:
            playerHands[1].append(p2)
            playerHands[1].append(p1)
        if len(playerHands[0]) == 0:
            return 1
        if len(playerHands[1]) == 0:
            return 0

def part2(playerHands):
    winner = play2(playerHands)
    return calculateScore(playerHands)[winner]

if __name__ == '__main__':
    with sc.fullscreen():
        with sc.location(0, 4):
            input = readInput('input.txt')
            result = part1(input)
            print('Part 1 score:', result)
            input = readInput('input.txt')
            result = part2(input)
            print('Part 2 valid:', result)
        
        with sc.location(5, 8):
            with sc.hidden_cursor():
                print('Press ESC to exit')
                wait_key(ESC)
