def generate_binaries(n: int):
    if n>1:
        return [bin+[0] for bin in generate_binaries(n-1)] + [bin+[1] for bin in generate_binaries(n-1)]
    else:
        return [[0], [1]]

with open("Advent-of-Code-2024/inputs/input07") as f:
    equations = [[int(eq[0]), [int(i) for i in eq[1].strip().split(' ')]] for eq in [l.strip().split(':') for l in f.readlines()]]

    res = 0

    for eq in equations:

        for operations in generate_binaries(len(eq[1]) - 1):

            value = eq[1][0]

            for i, operation in enumerate(operations):
                match operation:
                    case 0:
                        value += eq[1][i+1]
                    case 1:
                        value = value*eq[1][i+1]
                if value > eq[0]:
                    break
            
            if value == eq[0]:
                res += eq[0]
                break

    print(res)
