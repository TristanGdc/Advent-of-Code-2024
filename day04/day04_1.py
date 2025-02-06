def is_xmas(table, i, j):
    directions = [
        (0,1),      # right
        (0,-1),     # left
        (1,0),      # down
        (1,1),      # down right
        (1,-1),     # down left
        (-1,0),     # up
        (-1,1),     # up right
        (-1,-1)     # up left
    ]
    count = 0
    for dir in directions:
        index, x, y = 0, i+dir[0], j+dir[1]

        while (
            0 <= x < len(table) and\
            0 <= y < len(table[0])-1 and\
            table[x][y] == 'MAS'[index]
        ):
            index+=1
            if index == 3:
                print(dir, x, y)
                count+=1
                break
            x+=dir[0]
            y+=dir[1]

    return count

with open("Advent-of-Code-2024/day04/input04") as f:
    table = f.readlines()

    count = 0

    for i,line in enumerate(table):
        for j, char in enumerate(line):
            if char == 'X':
                count += is_xmas(table, i ,j)
    
    print(count)
