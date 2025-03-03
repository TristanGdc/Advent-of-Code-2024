def generate_ternaries(n: int):
    if n>1:
        return [bin+[0] for bin in generate_ternaries(n-1)] + [bin+[1] for bin in generate_ternaries(n-1)] + [bin+[2] for bin in generate_ternaries(n-1)]
    else:
        return [[0], [1], [2]]

with open("Advent-of-Code-2024/inputs/input07") as f:
    equations = [[int(eq[0]), [int(i) for i in eq[1].strip().split(' ')]] for eq in [l.strip().split(':') for l in f.readlines()]]

    res = 0

    for eq in equations:

        for operations in generate_ternaries(len(eq[1]) - 1):

            value = eq[1][0]

            for i, operation in enumerate(operations):
                match operation:
                    case 0:
                        value += eq[1][i+1]
                    case 1:
                        value = value*eq[1][i+1]
                    case 2:
                        value = int(str(value) + str(eq[1][i+1]))
                if value > eq[0]:
                    break
            
            if value == eq[0]:
                res += eq[0]
                break

    print(res)
