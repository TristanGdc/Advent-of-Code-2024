import numpy as np
directions = {
    '^' : np.array([-1, 0]),
    '>' : np.array([0, 1]),
    'v' : np.array([1, 0]),
    '<' : np.array([0,-1])
}

with open("Advent-of-Code-2024/inputs/input06") as f:
    area = np.array(list(map(lambda l : list(l.strip()) , f.readlines())))

    for i, l in enumerate(area):
        for j, char in enumerate(l):
            if char in directions.keys():
                guard_pos = np.array([i, j])

    is_out = False
    while not is_out:
        guard = area[*guard_pos]
        direction = directions[guard]

        while True:
            next_step_pos = guard_pos + direction

            try :
                if next_step_pos[0] < 0 or next_step_pos[1] < 0:
                    raise IndexError
                next_step = area[*next_step_pos]
            except IndexError:
                next_step = 'out'

            match next_step:
                case '.' | 'X':
                    area[*guard_pos] = 'X'
                    guard_pos = next_step_pos
                case '#':
                    keys = list(directions.keys())
                    next_guard = keys[(keys.index(guard)+1)%4]
                    area[*guard_pos] = next_guard
                    break
                case 'out':
                    area[*guard_pos] = 'X'
                    is_out = True
                    break
    
    print(np.count_nonzero(area == 'X'))
