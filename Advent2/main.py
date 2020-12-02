from console import sc
from console.constants import ESC
from console.utils import wait_key

class row:
    def __init__(self, min, max, letter, password):
        self.min = min
        self.max = max
        self.letter = letter
        self.password = password

def readInput(): 
    rows = []

    inputFile = open('input.txt')
    lines = inputFile.readlines()
    inputFile.close()

    for line in lines:
        columns=line.split(' ')
        minmax=columns[0].split("-")
        min=int(minmax[0])
        max=int(minmax[1])
        letter=columns[1][:1]
        password=columns[2].replace('\n','')
        rows.append(row(min, max, letter, password))
    return rows

def countValid1(rows):
    validCount = 0
    for row in rows:
        countLetter = 0
        for x in range(len(row.password)):
            if (row.password[x]==row.letter):
                countLetter = countLetter + 1
        if (countLetter >= row.min and countLetter <= row.max):
            validCount = validCount + 1  
    return validCount

def countValid2(rows):
    validCount = 0
    for row in rows:
        if ((row.password[row.min - 1] == row.letter) != (row.password[row.max - 1] == row.letter)):
            validCount = validCount + 1  
    return validCount


with sc.fullscreen():
    with sc.location(0, 4):
        input = readInput()
        result = countValid1(input)
        print('Policy 1 :', result)
        result = countValid2(input)
        print('Policy 2 :', result)
    
    with sc.location(5, 8):
        with sc.hidden_cursor():
            print('Press ESC to exit')
            wait_key(ESC)