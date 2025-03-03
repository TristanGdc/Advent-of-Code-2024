with open("Advent-of-Code-2024/inputs/input07") as f:
    equations = [[int(eq[0]), [int(i) for i in eq[1].strip().split(' ')]] for eq in [l.strip().split(':') for l in f.readlines()]]

    res = 0

    for eq in equations:

        values = [eq[1][0]]

        for m in eq[1][1:]:
            new_values = [value + m for value in values] + [value * m for value in values]
            values = new_values
        
        if eq[0] in values:
            res += eq[0]

    print(res)
