import numpy as np

with open("Advent-of-Code-2024/inputs/input08") as f:
    area = np.array([list(l.strip()) for l in f.readlines()])

    antenna_pos = {}
    antinode_positions = []

    for i, line in enumerate(area):
        for j, char in enumerate(line):

            if char != '.':
                current_pos = np.array([i, j])

                if char in antenna_pos.keys():
                    for pos in antenna_pos[char]:

                        try:
                            antinode_pos = 2 * current_pos - pos
                            if antinode_pos[0] < 0 or antinode_pos[1] < 0:
                                raise IndexError
                            if area[*antinode_pos] and not list(antinode_pos) in antinode_positions:
                                antinode_positions.append(list(antinode_pos))
                        except IndexError:
                            pass
                        try:
                            antinode_pos = 2 * pos - current_pos
                            if antinode_pos[0] < 0 or antinode_pos[1] < 0:
                                raise IndexError
                            if area[*antinode_pos] and not list(antinode_pos) in antinode_positions:
                                antinode_positions.append(list(antinode_pos))
                        except IndexError:
                            pass
                    
                    antenna_pos[char].append(current_pos)
                else:
                    antenna_pos[char] = [current_pos]

    print(len(antinode_positions))
            