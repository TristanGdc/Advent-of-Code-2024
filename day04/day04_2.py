def is_xmas(table, i, j):
    diag_1 = (table[i-1][j-1], table[i+1][j+1])
    diag_2 = (table[i+1][j-1], table[i-1][j+1])

    return ( diag_1 == ('M', 'S') or diag_1 == ('S', 'M') ) and (diag_2 == ('M', 'S') or diag_2 == ('S', 'M') )


with open("Advent-of-Code-2024/day04/input04") as f:
    table = f.readlines()

    count = 0

    for i,line in enumerate(table):
        for j, char in enumerate(line):
            if (
                char == 'A' and\
                0 < i < len(table)-1 and\
                0 < j < len(table[0])-2
            ):
                if is_xmas(table, i ,j):
                    count += 1
    
    print(count)
    