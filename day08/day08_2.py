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

                        v1 = current_pos - pos
                        v_pos = pos.copy()
                        while True:
                            try:
                                v_pos = v_pos + v1
                                if v_pos[0] < 0 or v_pos[1] < 0:
                                    raise IndexError
                                if area[*v_pos] and not list(v_pos) in antinode_positions:
                                    antinode_positions.append(list(v_pos))
                            except IndexError:
                                break

                        v2 = pos - current_pos
                        v_pos = current_pos.copy()
                        while True:
                            try:
                                v_pos = v_pos + v2
                                if v_pos[0] < 0 or v_pos[1] < 0:
                                    raise IndexError
                                if area[*v_pos] and not list(v_pos) in antinode_positions:
                                    antinode_positions.append(list(v_pos))
                            except IndexError:
                                break
                    
                    antenna_pos[char].append(current_pos)
                else:
                    antenna_pos[char] = [current_pos]

    print(len(antinode_positions))
            