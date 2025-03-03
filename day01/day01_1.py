with open("Advent-of-Code-2024/inputs/input01") as f:
    lines = f.readlines()

    left = []
    right = []

    for line in lines:
        cleared_line = list(map(lambda x: int(x.strip()), line.split('   ')))
        left.append(cleared_line[0])
        right.append(cleared_line[1])
    
    left.sort()
    right.sort()

    result = 0

    for i in range(len(left)):
        result += abs(right[i]-left[i])

    print(result)  
