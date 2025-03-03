import numpy as np

directions = {
    '^' : np.array([-1, 0]),
    '>' : np.array([0, 1]),
    'v' : np.array([1, 0]),
    '<' : np.array([0, -1])
}

def get_next_direction(direction):
    match list(direction):
        case [-1, 0]:
            return [0,1]
        case [0, 1]:
            return [1,0]
        case [1, 0]:
            return [0, -1]
        case [0, -1]:
            return [-1, 0]

def rindex(li: list, x):
    for i, element in enumerate(reversed(li)):
        if element == x:
            return len(li) - i - 1
    raise ValueError

def is_looping(li: list):
    last_item = li[-1]
    limit_index = len(li) - 1
    for k in range(li[:-1].count(last_item)):
        limit_index = rindex(li[:limit_index], last_item)
        posible_loop_size = len(li) - limit_index -1
        if len(li) >= posible_loop_size*2:
            if li[-posible_loop_size:] == li[-(posible_loop_size*2):-(posible_loop_size)]:
                return posible_loop_size
    return False

def step(area: np.array, pos: np.array, direction: np.array):
    posible_new_pos = pos + direction

    if (not 0 <= posible_new_pos[0] < len(area)) or (not 0 <= posible_new_pos[1] < len(area[0])):
        new_cell = 'out'
    else:
        new_cell = area[*posible_new_pos]

    match new_cell:
        case '.':
            return posible_new_pos, direction
        case '#' | 'O':
            new_direction = get_next_direction(direction)
            return step(area, pos, new_direction)
        case 'out':
            raise StopIteration()

with open("Advent-of-Code-2024/inputs/input06") as f:
    area = np.array(list(map(lambda l : list(l.strip()) , f.readlines())))

    for i, l in enumerate(area):
        for j, char in enumerate(l):
            if char in directions.keys():
                guard_pos = np.array([i, j])
                direction = directions[area[*guard_pos]]
                area[i, j] = '.'

    loops = []
    not_loops = []

    while True:
        try:
            next_pos, next_direction = step(area, guard_pos, direction)

            if not list(next_pos) in loops + not_loops:
                area[*next_pos] = 'O'
                test_pos, test_direction = guard_pos.copy(), direction.copy()
                turns = []

                while True:
                    try:
                        next_test_pos, next_test_direction = step(area, test_pos, test_direction)

                        if not np.array_equal(next_test_direction, test_direction):
                            turns.append(list(test_pos))
                            if is_looping(turns):
                                loops.append(list(next_pos))
                                break
                        
                        test_pos, test_direction = next_test_pos, next_test_direction

                    except StopIteration:
                        not_loops.append(list(next_pos))
                        break

                area[*next_pos] = '.'

        except StopIteration:
                break

        guard_pos, direction = next_pos, next_direction

    print(len(loops))
