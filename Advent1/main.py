def readInput(): 
    values = []

    inputFile = open('input.txt')
    lines = inputFile.readlines()
    inputFile.close()

    for line in lines:
        values.append(int(line))
    
    return values

def part1(values):
    for value1 in values:
        for value2 in values:
            if(value1 + value2 == 2020):
                print(value1, value2, value1 * value2)
                return

def part2(values):
    for value1 in values:
        for value2 in values:
            if (value1 + value2 >= 2020):
                break

            for value3 in values:
                if(value1 + value2 + value3 == 2020):
                    print(value1, value2, value3, value1 * value2 * value3)
                    return

values = readInput()
part1(values)
part2(values)
