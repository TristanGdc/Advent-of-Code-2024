with open("Advent-of-Code-2024/day01/input01") as f:
    lines = f.readlines()

    left = []
    right = []

    for line in lines:
        cleared_line = list(map(lambda x: int(x.strip()), line.split('   ')))
        left.append(cleared_line[0])
        right.append(cleared_line[1])
    
    coeff = [right.count(x) for x in left]

    result = 0

    for i in range(len(left)):
        result += left[i]*coeff[i]

    print(result)  
